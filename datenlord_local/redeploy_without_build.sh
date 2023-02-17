# run in prj root dir
kind delete cluster
kind create cluster --config ./paTools/k8s_kind/kind-config.yaml

kind load docker-image datenlord/datenlord:e2e_test
sh ./temp.sh