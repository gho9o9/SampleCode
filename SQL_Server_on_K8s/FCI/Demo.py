

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
# # 2. PV確認
#%% [markdown]
%%bash
cat ~/Jupyter/SQL_Server_on_K8s/FCI/pvc.yaml

#%% [markdown]
%%bash
kubectl get sc -o wide
kubectl describe sc azure-disk

#%% [markdown]
%%bash
kubectl get pv -o wide -n mssql-fci
kubectl describe pv -n mssql-fci

#%% [markdown]
%%bash
kubectl get pvc -o wide -n mssql-fci
kubectl describe pvc -n mssql-fci

#%% [markdown]
%%bash
az disk list -g MC_RG_BDC_O9O9AKS_JAPANEAST 

#%% [markdown]
# # 3. Pod確認
#%% [markdown]
%%bash
cat ~/Jupyter/SQL_Server_on_K8s/FCI/sql19deployment.yaml

#%% [markdown]
%%bash
kubectl get pod -o wide -n mssql-fci
kubectl describe pod -n mssql-fci

#%% [markdown]
%%bash
kubectl get service -o wide -n mssql-fci
kubectl describe service -n mssql-fci

#%% [markdown]
# # 4. SQL接続テスト
#%% [markdown]
%%bash
kubectl exec mssql-deployment-79fdff6b95-nk8zx -c mssql -n mssql-fci -- /opt/mssql-tools/bin/sqlcmd -U sa -P $PASSWORD -Q 'SELECT @@VERSION'
#%% [markdown]
%%bash
sqlcmd -S 52.185.174.22 -U sa -P $PASSWORD  -Q 'select @@version'
#%% [markdown]
%%bash
sqlcmd -S 52.185.174.22 -U sa -P $PASSWORD  -Q 'create database FCIDB'
sqlcmd -S 52.185.174.22 -U sa -P $PASSWORD  -Q 'use FCIDB; create table tab01(id int, name varchar(max)); insert into tab01 values (1, "SQL Server runs on K8s!")'
sqlcmd -S 52.185.174.22 -U sa -P $PASSWORD  -Q 'use FCIDB; select * from tab01'

#%% [markdown]
#kubectl exec mssql-deployment-79fdff6b95-ldwps -c mssql -n mssql-fci -- /opt/mssql-tools/bin/sqlcmd -U sa -P $PASSWORD -Q 'create database FCIDB'
#kubectl exec mssql-deployment-79fdff6b95-ldwps -c mssql -n mssql-fci -- /opt/mssql-tools/bin/sqlcmd -U sa -P $PASSWORD -Q 'use FCIDB; create table tab01(id int, name varchar(max)); insert into tab01 values (1, "SQL Server runs on K8s!")'
#kubectl exec mssql-deployment-79fdff6b95-ldwps -c mssql -n mssql-fci -- /opt/mssql-tools/bin/sqlcmd -U sa -P $PASSWORD -Q 'select name from sys.databases; use FCIDB; select * from tab01'
#sqlcmd -S localhost,11433 -U sa -P $PASSWORD -Q 'create database FCIDB'
#sqlcmd -S localhost,11433 -U sa -P $PASSWORD -Q 'use FCIDB; create table tab01(id int, name varchar(max)); insert into tab01 values (1, "SQL Server runs on K8s!")'
#sqlcmd -S localhost,11433 -U sa -P $PASSWORD -Q 'select name from sys.databases; use FCIDB; select * from tab01'

#%% [markdown]
# # 5. Pod障害擬似
#%% [markdown]
%%bash
kubectl get pod -o wide -n mssql-fci

#%% [markdown]
%%bash
kubectl delete pod mssql-deployment-79fdff6b95-nk8zx

#%% [markdown]
%%bash
kubectl get pod -o wide -n mssql-fci

#%% [markdown]
%%bash
sqlcmd -S 52.185.174.22 -U sa -P $PASSWORD  -Q 'use FCIDB; select * from tab01'



M-x shell
C-x o
C-x 0
C-x 2
C-u M-x shell -> shell2
C-x o
C-x o
C-x 0
