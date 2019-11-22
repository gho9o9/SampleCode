

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
%%bash
kubectl get node -o wide
az vm list -g MC_RG_BDC_O9O9AKS_JAPANEAST -d
az aks show -g rg_bdc -n o9o9aks
az aks browse -g rg_bdc --listen-address 0.0.0.0 -n o9o9aks

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
kubectl get pod -o wide -n mssql-ag
kubectl get pvc -o wide -n mssql-ag
# kubectl describe pvc -n mssql-ag
az disk list -g MC_RG_BDC_O9O9AKS_JAPANEAST
kubectl get service -o wide -n mssql-ag

# AG確認（DMV）
sqlcmd -S 40.115.179.101 -U sa -P $PASSWORD -Q 'select r.replica_server_name, rs.is_primary_replica, rs.synchronization_health_desc FROM sys.dm_hadr_database_replica_states rs JOIN sys.availability_replicas r ON r.group_id = rs.group_id AND r.replica_id = rs.replica_id'
# AG確認（SSMS）
# AG確認（K8s Dashboard）
az aks browse -g rg_bdc --listen-address 0.0.0.0 -n o9o9aks

# セカンダリから接続（ReadOnlyでないとエラーになる）
sqlcmd -S 20.43.76.137 -U sa -P $PASSWORD -Q 'use agdb; select * from tab01'
sqlcmd -S 20.43.76.137 -U sa -P $PASSWORD -Q 'use agdb; select * from tab01' -K READONLY

# AGの機能でフェールオーバー（エラーになる）
sqlcmd -S 40.115.179.101 -U sa -P $PASSWORD -Q 'ALTER AVAILABILITY GROUP agdb FAILOVER'

kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/AG/4-1.failover_to_mssql1-0.yaml -n mssql-ag
kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/AG/4-2.failover_to_mssql2-0.yaml -n mssql-ag
kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/AG/4-3.failover_to_mssql3-0.yaml -n mssql-ag

kubectl get jobs -n mssql-ag

# AG確認
sqlcmd -S 40.115.179.101 -U sa -P $PASSWORD -Q 'select r.replica_server_name, rs.is_primary_replica, rs.synchronization_health_desc FROM sys.dm_hadr_database_replica_states rs JOIN sys.availability_replicas r ON r.group_id = rs.group_id AND r.replica_id = rs.replica_id'

sqlcmd -S 40.115.179.101 -U sa -P $PASSWORD -Q 'select @@servername'

sqlcmd -S 20.43.76.137 -U sa -P $PASSWORD -Q 'select @@servername'

kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/AG/4-1.failover_to_mssql1-0.yaml -n mssql-ag
kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/AG/4-2.failover_to_mssql2-0.yaml -n mssql-ag
kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/AG/4-3.failover_to_mssql3-0.yaml -n mssql-ag


# pod障害

M-x shell
C-x o
C-x 0
C-x 2
C-u M-x shell -> shell2
C-x o
C-x o
C-x 0


	○ session1（pod監視）
	kubectl get pod -o wide -n mssql-fci -w

	○ session2（pod障害疑似）
	kubectl get pod -o wide -n mssql-fci
	kubectl delete pod <pod>
	sqlcmd -S 40.115.245.30 -U sa -P $SAPASSWORD  -Q 'select @@version'


# %%
