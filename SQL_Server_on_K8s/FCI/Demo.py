

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
# ![](image/2019-11-24-22-12-50.png)

#%% [markdown]
# # 1. 事前に準備済みのK8s環境を確認
#%% [markdown]
# ## 1-1. Cluster

#%%
%%bash
az aks show -g rg_bdc -n o9o9aks

#%%
%%bash
az aks browse -g rg_bdc --listen-address 0.0.0.0 -n o9o9aks
#%% [markdown]
# ![](image/2019-11-25-15-43-14.png)

#%% [markdown]
# ## 1-2. Node
#%%
%%bash
kubectl get node -o wide
#%%
%%bash
az vm list -g MC_RG_BDC_O9O9AKS_JAPANEAST -d
#%%
%%bash
kubectl describe node

#%% [markdown]
# # 2. PVC確認
#%%
%%bash
cat ~/Jupyter/SQL_Server_on_K8s/FCI/pvc.yaml

#%%
%%bash
kubectl get sc -o wide
#%%
%%bash
kubectl describe sc azure-disk

#%%
%%bash
kubectl get pv -o wide -n mssql-fci
#%%
%%bash
kubectl describe pv -n mssql-fci

#%%
%%bash
kubectl get pvc -o wide -n mssql-fci
#%%
%%bash
kubectl describe pvc -n mssql-fci

#%%
%%bash
az disk list -g MC_RG_BDC_O9O9AKS_JAPANEAST 

#%% [markdown]
# # 3. Pod確認
#%%
%%bash
cat ~/Jupyter/SQL_Server_on_K8s/FCI/sql19deployment.yaml

#%%
%%bash
kubectl get pod -o wide -n mssql-fci
#%%
%%bash
kubectl describe pod -n mssql-fci

#%%
%%bash
kubectl get service -o wide -n mssql-fci
#%%
%%bash
kubectl describe service -n mssql-fci

#%% [markdown]
# # 4. SQL接続テスト
#%%
%%bash
kubectl exec mssql-deployment-79fdff6b95-7jnt8 -c mssql -n mssql-fci -- /opt/mssql-tools/bin/sqlcmd -U sa -P $PASSWORD -Q 'SELECT @@VERSION'
#%%
%%bash
sqlcmd -S 52.185.169.168 -U sa -P $PASSWORD  -Q 'select @@version'
#%%
%%bash
sqlcmd -S 52.185.169.168 -U sa -P $PASSWORD  -Q 'create database FCIDB'
sqlcmd -S 52.185.169.168 -U sa -P $PASSWORD  -Q 'use FCIDB; create table tab01(id int, name varchar(max)); insert into tab01 values (1, "SQL Server runs on K8s!")'
sqlcmd -S 52.185.169.168 -U sa -P $PASSWORD  -Q 'use FCIDB; select * from tab01'

#%%
#kubectl exec mssql-deployment-79fdff6b95-ldwps -c mssql -n mssql-fci -- /opt/mssql-tools/bin/sqlcmd -U sa -P $PASSWORD -Q 'create database FCIDB'
#kubectl exec mssql-deployment-79fdff6b95-ldwps -c mssql -n mssql-fci -- /opt/mssql-tools/bin/sqlcmd -U sa -P $PASSWORD -Q 'use FCIDB; create table tab01(id int, name varchar(max)); insert into tab01 values (1, "SQL Server runs on K8s!")'
#kubectl exec mssql-deployment-79fdff6b95-ldwps -c mssql -n mssql-fci -- /opt/mssql-tools/bin/sqlcmd -U sa -P $PASSWORD -Q 'select name from sys.databases; use FCIDB; select * from tab01'
#sqlcmd -S localhost,11433 -U sa -P $PASSWORD -Q 'create database FCIDB'
#sqlcmd -S localhost,11433 -U sa -P $PASSWORD -Q 'use FCIDB; create table tab01(id int, name varchar(max)); insert into tab01 values (1, "SQL Server runs on K8s!")'
#sqlcmd -S localhost,11433 -U sa -P $PASSWORD -Q 'select name from sys.databases; use FCIDB; select * from tab01'

#%% [markdown]
# # 5. Pod障害擬似
#%%
%%bash
kubectl get pod -o wide -n mssql-fci

#%%
%%bash
kubectl delete pod mssql-deployment-79fdff6b95-7jnt8 -n mssql-fci

#%%
%%bash
kubectl get pod -o wide -n mssql-fci

#%%
%%bash
sqlcmd -S 52.185.169.168 -U sa -P $PASSWORD  -Q 'use FCIDB; select * from tab01'
#%%
%%bash
sqlcmd -S 52.185.169.168 -U sa -P $PASSWORD  -Q 'use master; drop database FCIDB'


#%%
M-x shell
C-x o
C-x 0
C-x 2
C-u M-x shell -> shell2
C-x o
C-x o
C-x 0
