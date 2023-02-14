1. install kind
```
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```
2. create kind cluster
KIND_NODE_VERSION: kindest/node:v1.21.1@sha256:69860bda5563ac81e3c0057d654b5253219618a22ec3a346306239bba8cfa1a6
```
cat >> ./kind-config.yaml <<END
          # Kind cluster with 1 control plane node and 3 workers
          kind: Cluster
          apiVersion: kind.x-k8s.io/v1alpha4
          nodes:
          # the control plane node config
          - role: control-plane
          # the three workers
          - role: worker
            image: kindest/node:v1.21.1@sha256:69860bda5563ac81e3c0057d654b5253219618a22ec3a346306239bba8cfa1a6
          - role: worker
            image: kindest/node:v1.21.1@sha256:69860bda5563ac81e3c0057d654b5253219618a22ec3a346306239bba8cfa1a6
          - role: worker
            image: kindest/node:v1.21.1@sha256:69860bda5563ac81e3c0057d654b5253219618a22ec3a346306239bba8cfa1a6
          END
(root)
kind create cluster --config ./kind-config.yaml
```