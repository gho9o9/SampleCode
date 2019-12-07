

#%%[markdown]
# # Markdown h1
# ## Markdown h2
# ### Markdown h3
# - Markdown 1
# - Markdown 2
# - Markdown 3
# # Image
# ![](image/2019-09-29-01-47-54.png)
# [label](url)

#%% [markdown]
# # 1. BDC環境確認

#%% [markdown]
# ## 1-1. K8s
#%%
%%bash
az aks show -g rg_aks -n o9o9aks
#%%
%%bash
az aks browse -g rg_aks --listen-address 0.0.0.0 -n o9o9aks

#%% [markdown]
# ## 1-2. Node
#%%
%%bash
az vmss list
#%%
%%bash
kubectl get node -o wide

#%% [markdown]
# ## 1-3. BDC [参考](https://docs.microsoft.com/ja-jp/sql/big-data-cluster/view-cluster-status?view=sql-server-ver15)
# ![](image/2019-12-07-22-08-37.png)
# ![](image/2019-12-07-22-09-29.png)

#%%
%%bash
azdata login --auth basic -n mssql-cluster -u o9o9
#%% [markdown]
# ### ステータス
%%bash
azdata bdc status show 
# azdata bdc control status show --all
# azdata bdc sql status show --all
# azdata bdc hdfs status show --all
# azdata bdc spark status show --all

#%% [markdown]
# ### エンドポイント
%%bash
azdata bdc endpoint list -o table

#%% [markdown]
# ### ADS Dashboard
# ![](image/2019-12-05-23-10-37.png)
# ![](image/2019-12-05-23-12-32.png)

#%% [markdown]
# ### Grafana
# ![](image/2019-12-05-23-13-05.png)
# ![](image/2019-12-05-23-13-25.png)

#%% [markdown]
# ### Kibana
# ![](image/2019-12-05-23-14-50.png)


#%% [markdown]
# ## 1-4. Pod [参考](https://docs.microsoft.com/ja-jp/sql/big-data-cluster/cluster-troubleshooting-commands?view=sql-server-ver15)
#%%
%%bash
kubectl get pods -n mssql-cluster
# podの詳細
# kubectl describe pod <pod_name> -n mssql-cluster
# podのログ取得
# kubectl logs <pod_name> --all-containers=true -n mssql-cluser > containers-log.txt
# kubectl logs <pod_name> -c <container_name> -n mssql-cluser > container-log.txt

#%% [markdown]
# ## 1-5. Service
#%%
%%bash
kubectl get svc -n mssql-cluster
# サービス詳細
# kubectl describe service <service_name> -n mssql-cluster

#%%
# ## 1-6. Container
# kubectl exec -it <pod_name>  -c <container_name> -n <namespace_name> -- /bin/bash <command name> 


#%% [markdown]
# # 2. Data Virtualization
# ![](image/2019-12-07-22-09-54.png)

#%% [markdown]
# # 2-1. Create external table from Azure SQL Database

#%%
%%bash
cat /etc/odbcinst.ini
#%%
import pyodbc
print(pyodbc.drivers())
%load_ext sql

#%%bash
kubectl get service -n mssql-cluster | grep 31433

#%%
#%sql mssql+pyodbc://o9o9:$PASSWORD@<master node ext ip>,31433/master?DRIVER={ODBC+Driver+17+for+SQL+Server}
%sql mssql+pyodbc://o9o9:$PASSWORD@52.137.100.239,31433/sales?DRIVER={ODBC+Driver+17+for+SQL+Server}

#%%
%sql select \
    @@version

#%%
%sql CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'MySQLBigData2019'

#%%
%sql CREATE DATABASE SCOPED CREDENTIAL SQLCred \
   WITH IDENTITY = 'o9o9', Secret = 'MySQLBigData2019';

#%%
%sql DROP EXTERNAL DATA SOURCE SQLServerInstance

#%%
%sql CREATE EXTERNAL DATA SOURCE SQLServerInstance \
WITH ( \
LOCATION = 'sqlserver://o9o9mssql.database.windows.net', \
-- PUSHDOWN = ON | OFF, \
   CREDENTIAL = SQLCred \
   , CONNECTION_OPTIONS='Database=wwi_commerce'  \
);

#%%
%sql CREATE EXTERNAL TABLE dbo.SQLReviews(
   [product_id] [bigint] NOT NULL,
   [customer_id] [bigint] NOT NULL,
   [review] [nvarchar](1000) NOT NULL,
   [date_added] [datetime] NOT NULL
   )
   WITH (
   LOCATION='wwi_commerce.dbo.Reviews',
   DATA_SOURCE=SqlServerInstance
   );

   select * from sqlreviews


#%%
# 参考
#mssql+pyodbc://user:password@server/database?DRIVER={enty in /etc/odbcinst.ini}'
# odbcinst.iniのDSN名のスペースは+に置換して指定する必要がある。
%sql mssql+pyodbc://o9o9:$PASSWORD@o9o9mssql.database.windows.net/master?DRIVER={ODBC+Driver+17+for+SQL+Server}
# もしくはライブラリパス直指定でもOK
#%sql mssql+pyodbc://o9o9:$PASSWORD@o9o9mssql.database.windows.net/master?DRIVER={/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.4.so.2.1}

#%%
%sql select @@version


# ![](image/2019-12-07-22-09-29.png)



# %%
