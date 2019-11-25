
#%% [markdown]
# # 環境廃棄
%%bash
kubectl delete namespace mssql-ag
# kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/AG/4-1.failover_to_mssql1-0.yaml -n mssql-ag
# kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/AG/4-2.failover_to_mssql2-0.yaml -n mssql-ag
# kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/AG/4-3.failover_to_mssql3-0.yaml -n mssql-ag
# kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/AG/3.ag-services.yaml -n mssql-ag
# kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/AG/2.sqlserver.yaml -n mssql-ag
# kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/AG/1.operator.yaml -n mssql-ag
# kubectl delete secret sql-secrets -n mssql-ag

#%%
