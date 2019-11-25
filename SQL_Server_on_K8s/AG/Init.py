#%% [markdown]
# # 1. AG用のnamespace作成
%%bash
kubectl create namespace mssql-ag

#%% [markdown]
# # 2. AG用のsecret作成
%%bash
kubectl create secret generic sql-secrets --from-literal=sapassword=$PASSWORD --from-literal=masterkeypassword=$PASSWORD -n mssql-ag

#%% [markdown]
# # 3. operator作成
%%bash
cat ~/Jupyter/SQL_Server_on_K8s/AG/1.operator.yaml
#%%
%%bash
kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/AG/1.operator.yaml -n mssql-ag

#%% [markdown]
# # 4. pod作成
%%bash
cat ~/Jupyter/SQL_Server_on_K8s/AG/2.sqlserver.yaml
#%%
%%bash
kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/AG/2.sqlserver.yaml -n mssql-ag

#%% [markdown]
# # 5. Service定義
%%bash
cat ~/Jupyter/SQL_Server_on_K8s/AG/3.ag-services.yaml
#%%
%%bash
kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/AG/3.ag-services.yaml -n mssql-ag

#%% [markdown]
# # 6. ag-primaryのExternalIPに接続
%%bash
sqlcmd -S 52.155.111.133 -U sa -P $PASSWORD -Q 'select @@servername'

#%% [markdown]
# # 7. AG用DB作成
%%bash
sqlcmd -S 52.155.111.133 -U sa -P $PASSWORD -Q 'create database agdb'
sqlcmd -S 52.155.111.133 -U sa -P $PASSWORD -Q 'use agdb; create table tab01(id int, name varchar(max)); insert into tab01 values (1, "AG on K8s!")'
sqlcmd -S 52.155.111.133 -U sa -P $PASSWORD -Q 'use agdb; select * from tab01'

#%% [markdown]
# # 8. DBフルバックアップ
%%bash
sqlcmd -S 52.155.111.133 -U sa -P $PASSWORD -Q 'backup database agdb to disk="/home/o9o9/agdb.bak" with format'

#%% [markdown]
# # 9. AGへ登録
%%bash
sqlcmd -S 52.155.111.133 -U sa -P $PASSWORD -Q 'use master; ALTER AVAILABILITY GROUP [mssql-ag] ADD DATABASE agdb'

# %%
