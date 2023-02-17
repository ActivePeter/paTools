# run in prj root dir
kind delete cluster
kind create cluster --config ./paTools/k8s_kind/kind-config.yaml
docker build . --build-arg RUST_IMAGE_VERSION=1.61.0 --file ./Dockerfile --target datenlord --tag datenlord/datenlord:e2e_test
kind load docker-image datenlord/datenlord:e2e_test
sh ./temp.sh