
#%% [markdown]
# # 環境廃棄
%%bash
kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/Basic/Understanding-K8s/chap03/deployment.yaml -n basic-k8s
kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/Basic/Understanding-K8s/chap03/service.yaml -n basic-k8s
kubectl delete namespace basic-k8s
