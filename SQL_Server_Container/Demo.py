

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
# # Demo準備
%%bash
sudo docker rm -f sql19rc1
sudo docker rm -f sql17cu16
sudo docker rm -f registry
sudo docker rmi localhost:5000/mssql/devdb:v1
sudo rm -r ~/SQL_Server_Container/DataVolume/*
sudo rm -r ~/SQL_Server_Container/Dockerfile
echo Cleanup

#%% [markdown]
# # Demo 1: SQL Server コンテナの実行
# ## 1-1.SQL Server 2017イメージをPull（事前にPull済み）
%%bash
sudo docker pull mcr.microsoft.com/mssql/server:2017-CU16
sudo docker image list | grep 2017-CU16

#%% [markdown]
# ## 1-2.SQL Server 2017コンテナ起動
%%bash
sudo docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=P@ssw0rd' -p 11433:1433 -v ~/SQL_Server_Container/DataVolume:/var/opt/mssql --name sql17cu16 -d mcr.microsoft.com/mssql/server:2017-CU16
sudo docker ps -a --filter name=sql17cu16
sleep 30

#%% [markdown]
# ## 1-3.コンテナ内でsqlcmdを実行（コンテナ内は1433ポートでリッスン）
%%bash
sudo docker exec sql17cu16 /opt/mssql-tools/bin/sqlcmd -S localhost,1433 -U sa -P P@ssw0rd -Q 'select @@version'

#%% [markdown]
# ## 1-4.コンテナ外でsqlcmd（ホストの11433ポートはコンテナの1433にマッピング）
%%bash
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'select @@version'

#%% [markdown]
# ## 1-5.DevDB作成
%%bash
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'create database DevDB'
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'use DevDB; create table tab01(id int, name varchar(max)); insert into tab01 values (1, "SQL Server runs on Docker!")'
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'select name from sys.databases; use DevDB; select * from tab01'

#%% [markdown]
# ## 1-6.コンテナ内にDBファイルが作成された
%%bash
sudo docker exec sql17cu16 ls -la /var/opt/mssql/data | grep DevDB

#%% [markdown]
# ## 1-7.ホストボリュームからもDBファイルが確認できる
%%bash
ls -la ~/SQL_Server_Container/DataVolume/data | grep DevDB

#%% [markdown]
# ## 1-8.コンテナ停止してもホストボリューム上のDBファイルは消えない
%%bash
sudo docker stop sql17cu16
sudo docker ps -a --filter name=sql17cu16
ls -la ~/SQL_Server_Container/DataVolume/data | grep DevDB

#%% [markdown]
# ## 1-9.コンテナ破棄してもホストボリューム上のDBファイルは消えない
%%bash
sudo docker rm -f sql17cu16
sudo docker ps -a --filter name=sql17cu16
ls -la ~/SQL_Server_Container/DataVolume/data | grep DevDB


#%% [markdown]
# # Demo 2: Docker コンテナ内での操作
# ## 2-1.SQL Server 2017コンテナ起動
%%bash
sudo docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=P@ssw0rd' -p 11433:1433 -v ~/SQL_Server_Container/DataVolume:/var/opt/mssql --name sql17cu16 -d mcr.microsoft.com/mssql/server:2017-CU16
sudo docker ps -a --filter name=sql17cu16
sleep 30

#%% [markdown]
# ## 2-2.コンテナ接続
# sudo docker exec -it sql17cu16 /bin/bash
# ## 2-3.コンテナ内でmssql-cliインストール
# > apt-get update
# > apt-get install mssql-cli
# ![](image/2019-10-08-23-26-04.png)
# > which mssql-cli
# > mssql-cli -S localhost -U sa -P P@ssw0rd
# ![](image/2019-10-08-23-29-40.png)

#%% [markdown]
# ## 2-4.ホスト側にはmssql-cliは存在しない
# /usr/bin/mssql-cli
# ![](image/2019-10-08-23-36-07.png)

#%% [markdown]
# ## 2-5.コンテナ破棄
%%bash
sudo docker rm -f sql17cu16
sudo docker ps -a --filter name=sql17cu16

#%% [markdown]
# # Demo 3: SQL Server コンテナ内のUpgrade（2017->2019）
# ## 3-1.SQL Server 2019イメージをPull（事前にPull済み）
%%bash
sudo docker pull mcr.microsoft.com/mssql/server:2019-RC1
sudo docker image list | grep 2019-RC1

#%% [markdown]
# ## 3-2.SQL Server2019コンテナ起動（SQL Server 2017で作成したデータファイルをマウント）
%%bash
sudo docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=P@ssw0rd' -p 11433:1433 -v ~/SQL_Server_Container/DataVolume:/var/opt/mssql --name sql19rc1 -d mcr.microsoft.com/mssql/server:2019-RC1
sudo docker ps -a --filter name=sql19rc1
sleep 30

#%% [markdown]
# ## 3-3.SQL Server に接続すると”Upgrade中だから待て”のエラー
# ### Sqlcmd: Error: Microsoft ODBC Driver 17 for SQL Server : Login failed for user 'sa'. Reason: Server is in script upgrade mode. Only administrator can connect at this time..
%%bash
sudo docker exec sql19rc1 /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P P@ssw0rd -Q 'select @@version'

#%% [markdown]
# ## 3-4.アップグレードが終われば接続できるようになる
# ### Microsoft SQL Server 2019 (RC1) - 15.0.1900.25 (X64)
%%bash
sudo docker exec sql19rc1 /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P P@ssw0rd -Q 'select @@version'

#%% [markdown]
# ## 3-5.SQL Server 2017から2019にアップグレードしたDBをSELECT
%%bash
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'use DevDB; select * from tab01'

#%% [markdown]
# # Demo 4: SQL Server コンテナ内のDBバックアップ
# ## 4-1.フルバックアップ
%%bash
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'backup database DevDB to disk="/tmp/DevDB.bak" with format'
sudo docker exec sql19rc1 ls -la /tmp/DevDB.bak

#%% [markdown]
# ## 4-2.バックアップをホストにコピー
%%bash
sudo docker cp sql19rc1:/tmp/DevDB.bak ~/SQL_Server_Container/DevDB.bak
ls -la ~/SQL_Server_Container/DevDB.bak

#%% [markdown]
# ## 4-3.DB削除＆DBファイル削除
%%bash
sudo docker rm -f sql19rc1
sudo docker ps -a --filter name=sql19rc1
sudo rm -r ~/SQL_Server_Container/DataVolume/*

#%% [markdown]
# # Demo 5: SQL Server カスタムコンテナイメージの作成と配布
# ## 5-1.Dockerfile編集
%%bash
cd ~/SQL_Server_Container
touch Dockerfile
echo 'FROM mcr.microsoft.com/mssql/server:2019-RC1' >> Dockerfile
echo 'COPY ./DevDB.bak /tmp/DevDB.bak' >> Dockerfile
echo 'CMD ["/opt/mssql/bin/sqlservr"]' >> Dockerfile
cat Dockerfile

#%% [markdown]
# ## 5-2.カスタムコンテナイメージのビルド
%%bash
cd ~/SQL_Server_Container
sudo docker build -t localhost:5000/mssql/devdb:v1 .
sudo docker history localhost:5000/mssql/devdb:v1
sudo docker image list | grep devdb

#%% [markdown]
# ## 5-3.ローカルプライベートレジストリ起動
%%bash
sudo docker run -d -p 5000:5000 --name registry -v ~/SQL_Server_Container/RegistryVolume:/var/lib/registry registry

#%% [markdown]
# ## 5-4.ローカルプライベートレジストリにプッシュ（事前プッシュ済みなので早い）
%%bash
sudo docker push localhost:5000/mssql/devdb:v1

#%% [markdown]
# ## 5-5.ローカルプライベートレジストリ確認
%%bash
wget http://localhost:5000/v2/_catalog -q -O /dev/stdout
wget http://localhost:5000/v2/mssql/devdb/tags/list -q -O /dev/stdout

#%% [markdown]
# ## 5-6.ローカルに作成したカスタムコンテナイメージを削除（明示的にプライベートレジストリからPULLするため）
%%bash
sudo docker rmi localhost:5000/mssql/devdb:v1
sudo docker image list

#%% [markdown]
# ## 5-7.ローカルプライベートレジストリから Pull & Run
%%bash
sudo docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=P@ssw0rd' -p 11433:1433 -v ~/SQL_Server_Container/DataVolume:/var/opt/mssql --name sql19rc1 -d localhost:5000/mssql/devdb:v1
sudo docker ps -a --filter name=sql19rc1
sudo docker image list | grep devdb

#%% [markdown]
# ## 5-8.カスタム（バックアップファイルを配置）を確認
%%bash
sudo docker exec sql19rc1 ls -l /tmp

#%% [markdown]
# # Demo 6: SQL Server カスタムコンテナへのDBリストア
# ## 6-1.SELECT（リストア前）
%%bash
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'use DevDB; select * from tab01'

#%% [markdown]
# ## 6-2.リストア
%%bash
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'RESTORE DATABASE [DevDB] FROM DISK = "/tmp/DevDB.bak"'

#%% [markdown]
# ## 6-3.SELECT
%%bash
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'use DevDB; select * from tab01'

#%% [markdown]
# # Demo 7: AutoTuning
# ## 7-1.手動チューニング
# ### 7-1-1.初期化
%%bash
sudo docker restart sqlautotune
sleep 10
sqlcmd -S localhost,61433 -U sa -P P@ssw0rd \
  -i ~/SQL_Server_Container/SQL_Server_Autotune/2.init_autotune_off.sql

#%% [markdown]
# ### 7-1-2.スループット収集
# Azure Data Studio で 3.batchrequests_perf_collector.sql を実行
# ![](image/2019-10-09-23-38-20.png)
# ### 7-1-3.ワークロード実行
# Azure Data Studio で 4.report.sql を実行
# ![](image/2019-10-09-23-39-50.png)
# ### 7-1-4.スループット推移確認
# Azure Data Studio で 5.batchrequests.sql を実行
# ![](image/2019-10-09-23-41-41.png)
# ### 7-1-5.パラメータスニッフィング問題発生
# Azure Data Studio で 6.regression.sql を実行
# ![](image/2019-10-09-23-42-59.png)
# ### 7-1-6.スループット推移確認(7-1-4に比較しスローダウンしていることを確認)
# Azure Data Studio で 5.batchrequests.sql を実行
# ![](image/2019-10-09-23-44-53.png)
# ### 7-1-7.チューニングの推奨を確認
# Azure Data Studio で 7.recommendations.sql を実行
# ![](image/2019-10-09-23-45-58.png)
# ### 7-1-8.推奨を手動適用
# Azure Data Studio で 8.manual_tune.sql を実行
# ![](image/2019-10-09-23-47-10.png)
# ### 7-1-9.スループット推移確認(スループットの改善を確認)
# Azure Data Studio で 5.batchrequests.sql を実行
# ![](image/2019-10-09-23-48-57.png)

#%% [markdown]
# ## 7-2.自動チューニング
# ### 7-2-1.初期化
%%bash
sudo docker restart sqlautotune
sleep 10
sqlcmd -S localhost,61433 -U sa -P P@ssw0rd \
  -i ~/SQL_Server_Container/SQL_Server_Autotune/2.init_autotune_on.sql

#%% [markdown]
# ### 7-2-2.スループット収集
# Azure Data Studio で 3.batchrequests_perf_collector.sql を実行
# ![](image/2019-10-09-23-38-20.png)
# ### 7-2-3.ワークロード実行
# Azure Data Studio で 4.report.sql を実行
# ![](image/2019-10-09-23-39-50.png)
# ### 7-2-4.スループット推移確認
# Azure Data Studio で 5.batchrequests.sql を実行
# ![](image/2019-10-09-23-56-40.png)
# ### 7-2-5.パラメータスニッフィング問題発生
# Azure Data Studio で 6.regression.sql を実行
# ![](image/2019-10-09-23-42-59.png)
# ### 7-2-6.スループット推移確認(7-2-4に比較しスローダウンしていることを確認)
# Azure Data Studio で 5.batchrequests.sql を実行
# ![](image/2019-10-09-23-58-20.png)
# ### 7-1-7.チューニングの推奨を確認
# Azure Data Studio で 7.recommendations.sql を実行
# ![](image/2019-10-09-23-59-43.png)
# ### 7-2-8.スループット推移確認(スループットの改善を確認)
# Azure Data Studio で 5.batchrequests.sql を実行
# ![](image/2019-10-10-00-17-54.png)
# ### 7-2-9.スループット推移確認([Reverted](https://docs.microsoft.com/ja-jp/sql/relational-databases/system-dynamic-management-views/sys-dm-db-tuning-recommendations-transact-sql?view=sql-server-2017#remarks)となるケースもあり)
# Azure Data Studio で 5.batchrequests.sql を実行
# ![](image/2019-10-10-00-14-19.png)

#%% [markdown]
# # コンテンツアップロード
%%bash
#scp -r ~/OneDrive/Tech/Sample/Public/SampleCode/SQL_Server_Container user@host:/home/o9o9/jupyter/SampleCode/SQL_Server_Container
