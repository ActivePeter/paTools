guide

https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/

my notes

https://hanbaoaaa.xyz/?noteid=1&x=-473&y=1247

container runtime

https://kubernetes.io/docs/setup/production-environment/container-runtimes/

```
su 

cd ./container_deploy

python ./deploy_container.py

cd ..

kubeadm init --config ./kubeadm-config.yaml 
```
---
network plugin returns error: cni plugin not initialized

```
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```
---
loadFlannelSubnetEnv failed: open /run/flannel/subnet.env: no such file or directory"

