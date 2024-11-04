# Test the helmchart with kind

```shell
cd helm
kind delete cluster || :
kind create cluster
helm dependency update
kubectl create ns imalive
helm template . --values values.yaml --namespace imalive | kubectl -n imalive apply -f -
kubectl -n imalive get pods
```
