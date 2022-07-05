# Testing Imalive with a K3D cluster

## k3d init cluster

```shell
k3d cluster create localdev --api-port 6550 -p "8089:8089@loadbalancer"
sudo k3d kubeconfig get localdev > ~/.kube/config 
```

## Install the helmchart

```shell
kubectl create ns imalive
cd helm
helm dependency update
helm create imalive
helm -n imalive install imalive -f values.yaml --generate-name
```

## Check the deployement

```shell
kubectl -n imalive get pods
curl localhost:8089 -v
```
