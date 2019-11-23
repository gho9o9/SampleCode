#%% [markdown]
# # AG用のnamespaceとsecret作成
# ## 1. Namespace & Secret 作成
%%bash
kubectl create namespace mssql-ag
kubectl create secret generic sql-secrets --from-literal=sapassword=$PASSWORD --from-literal=masterkeypassword=$PASSWORD -n mssql-ag

#%% [markdown]
# # 2. operator作成
%%bash
kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/AG/1.operator.yaml -n mssql-ag

#%% [markdown]
# # 3. pod作成
%%bash
kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/AG/2.sqlserver.yaml -n mssql-ag

#%% [markdown]
# # 4. Service定義
%%bash
kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/AG/3.ag-services.yaml -n mssql-ag

#%% [markdown]
# # 5. ag-primaryのExternalIPに接続
%%bash
sqlcmd -S 40.115.179.101 -U sa -P $PASSWORD -Q 'select @@servername'

#%% [markdown]
# # 6. AG用DB作成
%%bash
sqlcmd -S 40.115.179.101 -U sa -P $PASSWORD -Q 'create database agdb'
sqlcmd -S 40.115.179.101 -U sa -P $PASSWORD -Q 'use agdb; create table tab01(id int, name varchar(max)); insert into tab01 values (1, "AG on K8s!")'

#%% [markdown]
# # 7. DBフルバックアップ
%%bash
sqlcmd -S 40.115.179.101 -U sa -P $PASSWORD -Q 'backup database agdb to disk="/home/o9o9/agdb.bak" with format'

#%% [markdown]
# # 8. AGへ登録
%%bash
sqlcmd -S 40.115.179.101 -U sa -P $PASSWORD -Q 'use master; ALTER AVAILABILITY GROUP mssql-ag ADD DATABASE agdb'

# %%
