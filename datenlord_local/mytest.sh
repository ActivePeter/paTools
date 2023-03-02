cat <<EOF >datenlord-demo.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-datenlord-test
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 100Mi
  storageClassName: csi-datenlord-sc

---
apiVersion: v1
kind: Pod
metadata:
  name: my-datenlord-test
spec:
    containers:
    - name: lalala
      image: nginx
      volumeMounts:
      - mountPath: /usr/share/nginx/html
        name: data
    volumes:
    - name: data
      persistentVolumeClaim:
        claimName: pvc-datenlord-test
EOF

kubectl apply -f datenlord-demo.yaml