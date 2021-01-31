
#%% [markdown]
# # 環境廃棄
%%bash
kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/FCI/pvc.yaml -n mssql-fci
kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/FCI/sql19deployment.yaml -n mssql-fci
kubectl delete secret mssql -n mssql-fci
kubectl delete namespace mssql-fci
