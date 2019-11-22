

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
# # 2. PV作成
cd ~/Jupyter/SQL_Server_on_K8s/FCI
cat pvc.yaml
kubectl apply -f pvc.yaml -n mssql-fci

# # 3. PV確認 
kubectl get sc -o wide
kubectl describe sc azure-disk
kubectl get pv -o wide -n mssql-fci
kubectl describe pv -n mssql-fci
kubectl get pvc -o wide -n mssql-fci
kubectl describe pvc -n mssql-fci
az disk list -g MC_RG_BDC_O9O9AKS_JAPANEAST 

# # 4. SQL（Deployment、Service）作成
cat sql19deployment.yaml
kubectl apply -f sql19deployment.yaml -n mssql-fci

# # 5. SQL確認
kubectl get pod -o wide -n mssql-fci
kubectl describe pod -n mssql-fci
kubectl get service -o wide -n mssql-fci
kubectl describe service -n mssql-fci

# # 6. SQL接続テスト
kubectl exec mssql-deployment-79fdff6b95-ldwps -c mssql -n mssql-fci -- /opt/mssql-tools/bin/sqlcmd -U sa -P $PASSWORD -Q 'SELECT @@VERSION'
sqlcmd -S 52.185.174.22 -U sa -P $PASSWORD  -Q 'select @@version'
sqlcmd -S 52.185.174.22 -U sa -P $PASSWORD  -Q 'create database FCIDB'
sqlcmd -S 52.185.174.22 -U sa -P $PASSWORD  -Q 'use FCIDB; create table tab01(id int, name varchar(max)); insert into tab01 values (1, "SQL Server runs on K8s!")'
sqlcmd -S 52.185.174.22 -U sa -P $PASSWORD  -Q 'select name from sys.databases; use FCIDB; select * from tab01'
#kubectl exec mssql-deployment-79fdff6b95-ldwps -c mssql -n mssql-fci -- /opt/mssql-tools/bin/sqlcmd -U sa -P $PASSWORD -Q 'create database FCIDB'
#kubectl exec mssql-deployment-79fdff6b95-ldwps -c mssql -n mssql-fci -- /opt/mssql-tools/bin/sqlcmd -U sa -P $PASSWORD -Q 'use FCIDB; create table tab01(id int, name varchar(max)); insert into tab01 values (1, "SQL Server runs on K8s!")'
#kubectl exec mssql-deployment-79fdff6b95-ldwps -c mssql -n mssql-fci -- /opt/mssql-tools/bin/sqlcmd -U sa -P $PASSWORD -Q 'select name from sys.databases; use FCIDB; select * from tab01'

#sqlcmd -S localhost,11433 -U sa -P $PASSWORD -Q 'create database FCIDB'
#sqlcmd -S localhost,11433 -U sa -P $PASSWORD -Q 'use FCIDB; create table tab01(id int, name varchar(max)); insert into tab01 values (1, "SQL Server runs on K8s!")'
#sqlcmd -S localhost,11433 -U sa -P $PASSWORD -Q 'select name from sys.databases; use FCIDB; select * from tab01'


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
