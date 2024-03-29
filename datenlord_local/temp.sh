# 第一阶段，部署，判断是否正常挂载
kubectl cluster-info
kubectl get pods -A
kubectl apply -f ./snapshot.storage.k8s.io_volumesnapshots.yaml
kubectl apply -f ./snapshot.storage.k8s.io_volumesnapshotcontents.yaml
kubectl apply -f ./snapshot.storage.k8s.io_volumesnapshotclasses.yaml
kubectl apply -f scripts/datenlord.yaml
echo start1
# 等待启动完成
kubectl wait --for=condition=Ready pod -l app=csi-controller-datenlord -n csi-datenlord --timeout=140s
kubectl wait --for=condition=Ready pod -l app=csi-nodeplugin-datenlord -n csi-datenlord --timeout=60s
FOUND_PATH=`cat /proc/self/mountinfo | grep fuse | grep /var/opt/datenlord-data | awk '{print $5}'`
test -n $FOUND_PATH || (echo "FAILED TO FIND MOUNT PATH /var/opt/datenlord-data" && /bin/false)
kubectl delete -f scripts/datenlord.yaml
#判断delete后是否取消挂在
NO_PATH=`cat /proc/self/mountinfo | grep fuse | grep /var/opt/datenlord-data | awk '{print $5}'`
test -z $NO_PATH || (echo "FAILED TO UN-MOUNT PATH /var/opt/datenlord-data" && /bin/false)
# 重新开始
echo start2
kubectl apply -f scripts/datenlord.yaml
# 这几个还不清楚是啥
kubectl get csidriver
kubectl get csinode
kubectl get storageclass
kubectl get volumesnapshotclass
echo wait2
kubectl wait --for=condition=Ready pod -l app=csi-controller-datenlord -n csi-datenlord --timeout=140s
kubectl wait --for=condition=Ready pod -l app=csi-nodeplugin-datenlord -n csi-datenlord --timeout=60s

# snapshot controller
wget https://raw.githubusercontent.com/kubernetes-csi/external-snapshotter/v5.0.0/deploy/kubernetes/snapshot-controller/rbac-snapshot-controller.yaml
wget https://raw.githubusercontent.com/kubernetes-csi/external-snapshotter/v5.0.0/deploy/kubernetes/snapshot-controller/setup-snapshot-controller.yaml
sed -e 's/namespace\:\ default/namespace\:\ kube\-system/g' rbac-snapshot-controller.yaml > datenlord-rbac-snapshot-controller.yaml
sed -e 's/namespace\:\ default/namespace\:\ kube\-system/g' setup-snapshot-controller.yaml > datenlord-setup-snapshot-controller.yaml
docker pull gcr.io/k8s-staging-sig-storage/snapshot-controller:v5.0.0
kind load docker-image gcr.io/k8s-staging-sig-storage/snapshot-controller:v5.0.0
kubectl apply -f datenlord-rbac-snapshot-controller.yaml
kubectl apply -f datenlord-setup-snapshot-controller.yaml
for i in $(seq 1 30); do
if kubectl get deployment snapshot-controller -n kube-system; then
    break
fi 
sleep 1
done
kubectl wait --for=condition=Ready pod -l app=snapshot-controller -n kube-system --timeout=60s

# 打印信息
kubectl get pods -A -o wide
# Sleep 60 to wait cluster become stable
sleep 60
kubectl get pods -A -o wide
# sudo netstat -lntp && ls -lsh