

#%%[markdown]
# # Markdown h1
# ## Markdown h2
# ### Markdown h3
# - Markdown 1
# - Markdown 2
# - Markdown 3
# # Image
# ![](image/2019-09-29-01-47-54.png)

#%% [markdown]
# # 1. 事前に準備済みのK8s環境を確認
#%% [markdown]
# ## K8s
#%% [markdown]
%%bash
az aks show -g rg_bdc -n o9o9aks
#%% [markdown]
%%bash
az aks browse -g rg_bdc --listen-address 0.0.0.0 -n o9o9aks

#%% [markdown]
# ## Node
#%% [markdown]
%%bash
kubectl get node -o wide
#%% [markdown]
%%bash
az vm list -g MC_RG_BDC_O9O9AKS_JAPANEAST -d
#%% [markdown]
%%bash
kubectl describe node

#%% [markdown]
# # 2. operator作成
%%bash
cat ~/Jupyter/SQL_Server_on_K8s/AG/1.operator.yaml

#%% [markdown]
# # 3. pod作成
%%bash
cat ~/Jupyter/SQL_Server_on_K8s/AG/2.sqlserver.yaml

#%% [markdown]
# # 4. Service定義
%%bash
cat ~/Jupyter/SQL_Server_on_K8s/AG/3.ag-services.yaml

#%% [markdown]
# # 5. 環境確認
#%% [markdown]
%%bash
kubectl get pod -o wide -n mssql-ag
#%% [markdown]
%%bash
kubectl get pvc -o wide -n mssql-ag
# kubectl describe pvc -n mssql-ag
#%% [markdown]
%%bash
az disk list -g MC_RG_BDC_O9O9AKS_JAPANEAST
#%% [markdown]
%%bash
kubectl get service -o wide -n mssql-ag

#%% [markdown]
# # 6. AG確認（DMV）
#%% [markdown]
%%bash
sqlcmd -S 40.115.179.101 -U sa -P $PASSWORD -Q 'select r.replica_server_name, rs.is_primary_replica, rs.synchronization_health_desc FROM sys.dm_hadr_database_replica_states rs JOIN sys.availability_replicas r ON r.group_id = rs.group_id AND r.replica_id = rs.replica_id'
#%% [markdown]
%%bash
sqlcmd -S 40.115.179.101 -U sa -P $PASSWORD -Q 'select @@servername'
#%% [markdown]
%%bash
sqlcmd -S 20.43.76.137 -U sa -P $PASSWORD -Q 'select @@servername'

#%% [markdown]
# # 6. AG確認（SSMS）

#%% [markdown]
# # 6. AG確認（K8s Dashboard）
#%% [markdown]
%%bash
az aks browse -g rg_bdc --listen-address 0.0.0.0 -n o9o9aks

#%% [markdown]
# # 7.セカンダリから接続（ReadOnlyでないとエラーになる）
#%% [markdown]
%%bash
sqlcmd -S 20.43.76.137 -U sa -P $PASSWORD -Q 'use agdb; select * from tab01'
#%% [markdown]
%%bash
sqlcmd -S 20.43.76.137 -U sa -P $PASSWORD -Q 'use agdb; select * from tab01' -K READONLY

#%% [markdown]
# # 8. AGの機能でフェールオーバー（エラーになる）
#%% [markdown]
%%bash
sqlcmd -S 40.115.179.101 -U sa -P $PASSWORD -Q 'ALTER AVAILABILITY GROUP agdb FAILOVER'

#%% [markdown]
# # 9. K8sのJobでフェールオーバー
#%% [markdown]
%%bash
# kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/AG/4-1.failover_to_mssql1-0.yaml -n mssql-ag
kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/AG/4-2.failover_to_mssql2-0.yaml -n mssql-ag
# kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/AG/4-3.failover_to_mssql3-0.yaml -n mssql-ag
#%% [markdown]
%%bash
kubectl get jobs -n mssql-ag

#%% [markdown]
# # 10. AG確認
#%% [markdown]
%%bash
sqlcmd -S 40.115.179.101 -U sa -P $PASSWORD -Q 'select r.replica_server_name, rs.is_primary_replica, rs.synchronization_health_desc FROM sys.dm_hadr_database_replica_states rs JOIN sys.availability_replicas r ON r.group_id = rs.group_id AND r.replica_id = rs.replica_id'
#%% [markdown]
%%bash
sqlcmd -S 40.115.179.101 -U sa -P $PASSWORD -Q 'select @@servername'
#%% [markdown]
%%bash
sqlcmd -S 20.43.76.137 -U sa -P $PASSWORD -Q 'select @@servername'

#%% [markdown]
# # （11. F/Oジョブの削除）
#%% [markdown]
%%bash
# kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/AG/4-1.failover_to_mssql1-0.yaml -n mssql-ag
kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/AG/4-2.failover_to_mssql2-0.yaml -n mssql-ag
# kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/AG/4-3.failover_to_mssql3-0.yaml -n mssql-ag
#%% [markdown]
%%bash
kubectl get jobs -n mssql-ag


#%% [markdown]
# # （12. Primaryをmssql1−0に戻しておく）
#%% [markdown]
%%bash
kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/AG/4-1.failover_to_mssql1-0.yaml -n mssql-ag
kubectl get jobs -n mssql-ag
sqlcmd -S 40.115.179.101 -U sa -P $PASSWORD -Q 'select r.replica_server_name, rs.is_primary_replica, rs.synchronization_health_desc FROM sys.dm_hadr_database_replica_states rs JOIN sys.availability_replicas r ON r.group_id = rs.group_id AND r.replica_id = rs.replica_id'
kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/AG/4-1.failover_to_mssql1-0.yaml -n mssql-ag
kubectl get jobs -n mssql-ag