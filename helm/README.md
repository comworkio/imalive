# Testing Imalive with a K3D cluster

## k3d init cluster

```shell
k3d cluster create localdev --api-port 6550 -p "8089:80@loadbalancer"
sudo k3d kubeconfig get localdev > ~/.kube/config 
```

## Install the helmchart

```shell
cd helm # all the commands below must be under imalive/helm directory
kubectl create ns imalive
helm dependency update
helm -n imalive install . -f values.yaml --generate-name
```

## Check the deployement

```shell
kubectl -n imalive get pods
curl localhost:8089 -v
```
