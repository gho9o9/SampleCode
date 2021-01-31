

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
# # 2-1. master node に接続
#%% [markdown]
# ## 2−1−1. master node ext ip 確認 
#%%bash
kubectl get service -n mssql-cluster | grep 31433

#%% [markdown]
# ## 2−1−2. pyodbc接続
#%%
%%bash
cat /etc/odbcinst.ini
#%%
import pyodbc
print(pyodbc.drivers())
%load_ext sql
#%%
#%sql mssql+pyodbc://o9o9:$PASSWORD@<master node ext ip>,31433/master?DRIVER={ODBC+Driver+17+for+SQL+Server}
%sql mssql+pyodbc://o9o9:$PASSWORD@52.137.100.239,31433/sales?DRIVER={ODBC+Driver+17+for+SQL+Server}

#%% [markdown]
# # 2-2. 外部テーブル

#%% [markdown]
# ## 2−2-1. Cleanup
#%%
%sql DROP DATABASE SCOPED CREDENTIAL SQLCred
%sql DROP MASTER KEY
%sql DROP EXTERNAL DATA SOURCE SQLServerInstance
%sql DROP EXTERNAL TABLE dbo.SQLReviews
%sql DROP EXTERNAL FILE FORMAT [FileFormat_stockitemholdings]
%sql DROP EXTERNAL TABLE [dbo].[stockitemholdings]

#%% [markdown]
# ## 2−2-2. SQLDB

#%% [markdown]
# ## 1. master key 作成
#%%
%sql CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'P@ssw0rd'

#%% [markdown]
# ## 2. cred 作成
#%%
%sql CREATE DATABASE SCOPED CREDENTIAL SQLCred \
   WITH IDENTITY = 'o9o9', Secret = 'P@ssw0rd'

#%% [markdown]
# ## 3. SQLDB外部データソース作成
#%%
%sql CREATE EXTERNAL DATA SOURCE SQLServerInstance \
WITH ( \
LOCATION = 'sqlserver://o9o9mssql.database.windows.net', \
   CREDENTIAL = SQLCred \
   , CONNECTION_OPTIONS='Database=wwi_commerce'  \
);

#%% [markdown]
# ## 4. SQLDB外部テーブル作成
#%%
%sql CREATE EXTERNAL TABLE dbo.SQLReviews( \
   [product_id] [bigint] NOT NULL, \
   [customer_id] [bigint] NOT NULL, \
   [review] [nvarchar](1000) NOT NULL, \
   [date_added] [datetime] NOT NULL \
   ) \
   WITH ( \
   LOCATION='wwi_commerce.dbo.Reviews', \
   DATA_SOURCE=SqlServerInstance \
   );

#%% [markdown]
# ## 5. CSVファイルを外部テーブルを介してT-SQLでクエリ
#%%
%sql select * from dbo.SQLReviews


#%% [markdown]
# ## 2−2-3. CSV on HDFS
# ## 1. フォルダ作成
# ![](image/2019-12-08-13-57-58.png)
# ## 2. 作成したフォルダにCSVファイルをアップロード
# ![](image/2019-12-08-13-58-57.png)
# ![](image/2019-12-08-14-11-39.png)
# ## 3. CSVファイルに対して外部テーブルonストレージプールを定義
# ### T-SQL
#%%
%sql USE [sales]; \
    CREATE EXTERNAL FILE FORMAT [FileFormat_stockitemholdings] \
        WITH (FORMAT_TYPE = DELIMITEDTEXT, FORMAT_OPTIONS (FIELD_TERMINATOR = N',', STRING_DELIMITER = N'\"', FIRST_ROW = 2)); \
    CREATE EXTERNAL TABLE [dbo].[stockitemholdings] \
    ( \
        [StockItemID] smallint NOT NULL, \
        [QuantityOnHand] int NOT NULL, \
        [BinLocation] nvarchar(50) NOT NULL, \
        [LastStocktakeQuantity] int NOT NULL, \
        [LastCostPrice] float NOT NULL, \
        [ReorderLevel] tinyint NOT NULL, \
        [TargetStockLevel] smallint NOT NULL, \
        [LastEditedBy] tinyint NOT NULL, \
        [LastEditedWhen] nvarchar(50) NOT NULL \
    ) \
    WITH (LOCATION = N'/data/stockitemholdings.csv', DATA_SOURCE = [SqlStoragePool], FILE_FORMAT = [FileFormat_stockitemholdings]);
# ### GUI
# Azure Data Studio Extension（Data Vitualization）で GUI操作が可能
# ![](image/2019-12-08-14-48-11.png)
# ![](image/2019-12-08-14-51-16.png)
# ![](image/2019-12-08-14-51-41.png)
# ![](image/2019-12-08-14-52-30.png)
# ![](image/2019-12-08-14-52-49.png)
# ![](image/2019-12-08-15-05-03.png)
# ## 4. CSVファイルを外部テーブルを介してT-SQLでクエリ
#%%
%sql SELECT TOP (10) \
    [StockItemID] \
    ,[QuantityOnHand] \
    ,[BinLocation] \
    ,[LastStocktakeQuantity] \
    ,[LastCostPrice] \
    ,[ReorderLevel] \
    ,[TargetStockLevel] \
    ,[LastEditedBy] \
    ,[LastEditedWhen] \
    FROM [sales].[dbo].[stockitemholdings]

#%% [markdown]
# ## 2−2-4. 内部テーブルと外部テーブルのジョイン
#%%
%sql SELECT TOP (10) \
        i.i_item_sk AS ItemID \
        ,i.i_item_desc AS Item \
        ,c.c_first_name AS FirstName, c.c_last_name AS LastName \
        ,csv.QuantityOnHand \
        ,sqldb.review AS Review, sqldb.date_added AS DateReviewed \
    FROM dbo.item as i \
    JOIN dbo.SQLReviews AS sqldb ON i.i_item_sk = sqldb.product_id \
    JOIN dbo.customer AS c ON c.c_customer_sk = sqldb.customer_id \
    JOIN dbo.stockitemholdings AS csv ON i.i_item_sk = csv.StockItemID
# ![](image/2019-12-08-15-10-36.png)



#%% [markdown]
# # 2-3. データマート（データプールテーブル）

#%% [markdown]
# ## 2−2-2. Cleanup
#%%
%sql DROP EXTERNAL TABLE [web_clickstream_clicks_data_pool]
# ※. SSMSもしくはADSで実行が必要(ipythonから実行するとExternal Data Pool Table Drop operation statement cannot be used inside a user transaction.となる)

#%%
%sql DROP EXTERNAL FILE FORMAT csv_file

#%%
%sql DROP EXTERNAL TABLE [web_clickstreams_hdfs]

# ## 2−3−1. データプールテーブル定義
# ※. SSMSもしくはADSで実行が必要(ipythonから実行するとExternal Data Pool Table Create operation statement cannot be used inside a user transaction.となる)
#%%
%sql CREATE EXTERNAL TABLE [web_clickstream_clicks_data_pool] \
    ("wcs_click_date_sk" BIGINT \
    , "wcs_click_time_sk" BIGINT \
    , "wcs_sales_sk" BIGINT \
    , "wcs_item_sk" BIGINT \
    , "wcs_web_page_sk" BIGINT \
    , "wcs_user_sk" BIGINT \
    ) \
    WITH \
    ( \
    DATA_SOURCE = SqlDataPool, \
    DISTRIBUTION = ROUND_ROBIN \
    ) \
    GO

#%% [markdown]
# ## 2−3−2. 外部データフォーマット定義
#%%
%sql CREATE EXTERNAL FILE FORMAT csv_file \
    WITH (FORMAT_TYPE = DELIMITEDTEXT, \
          FORMAT_OPTIONS( \
              FIELD_TERMINATOR = ',', \
              STRING_DELIMITER = '"', \
              FIRST_ROW = 2, \
              USE_TYPE_DEFAULT = True) \
    )

#%% [markdown]
# ## 2−3−3. 外部テーブル定義
#%%
%sql CREATE EXTERNAL TABLE [web_clickstreams_hdfs] \
    ("wcs_click_date_sk" BIGINT \
    , "wcs_click_time_sk" BIGINT \
    , "wcs_sales_sk" BIGINT \
    , "wcs_item_sk" BIGINT \
    , "wcs_web_page_sk" BIGINT \
    , "wcs_user_sk" BIGINT) \
    WITH \
    ( \
        DATA_SOURCE = SqlStoragePool, \
        LOCATION = '/web_logs', \
        FILE_FORMAT = csv_file \
    )

#%% [markdown]
# ## 2−3−4. 外部データを外部テーブルを介してデータプールへロード
# ※. SSMSもしくはADSで実行が必要(ipythonから実行するとExternal Data Pool Table DML statement cannot be used inside a user transaction. となる)
#%%
%sql INSERT INTO web_clickstream_clicks_data_pool \
    SELECT wcs_click_date_sk \
        , wcs_click_time_sk \
        , wcs_sales_sk \
        , wcs_item_sk \
        , wcs_web_page_sk \
        , wcs_user_sk \
    FROM web_clickstreams_hdfs

#%% [markdown]
# ## 2−3−5. データプールをクエリ
#%%
%sql SELECT count(*) AS TotalRecords FROM [dbo].[web_clickstream_clicks_data_pool]
#%%
%sql SELECT TOP 10 * FROM [dbo].[web_clickstream_clicks_data_pool]
## %sql SELECT TOP 10 * FROM [dbo].[web_clickstreams_hdfs]




### DMVクエリ
### Sparkクエリ
### HDFS階層化



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
