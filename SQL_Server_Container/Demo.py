

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

#%% [markdown]
# # Demo 1: SQL Server コンテナの実行
# ## SQL Server 2017イメージは事前にPull済み
%%bash
sudo docker image list | grep 2017-CU16

#%% [markdown]
# ## SQL Server 2017コンテナ起動
%%bash
sudo docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=P@ssw0rd' -p 11433:1433 -v ~/SQL_Server_Container/DataVolume:/var/opt/mssql --name sql17cu16 -d mcr.microsoft.com/mssql/server:2017-CU16
sudo docker ps -a --filter name=sql17cu16

#%% [markdown]
# ## コンテナ内でsqlcmd
%%bash
sudo docker exec sql17cu16 /opt/mssql-tools/bin/sqlcmd -S localhost,1433 -U sa -P P@ssw0rd -Q 'select @@version'

#%% [markdown]
# ## コンテナ外でsqlcmd
%%bash
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'select @@version'

#%% [markdown]
# ## DevDBファイルはコンテナ内に存在しない
%%bash
sudo docker exec sql17cu16 ls -la /var/opt/mssql/data

#%% [markdown]
# ## DevDBファイルはコンテナ外にも存在しない
%%bash
ls -la ~/SQL_Server_Container/DataVolume/data

#%% [markdown]
# ## DevDB作成
%%bash
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'create database DevDB'
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'use DevDB; create table tab01(id int, name varchar(max)); insert into tab01 values (1, "SQL Server runs on Docker!")'
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'select name from sys.databases; use DevDB; select * from tab01'

#%% [markdown]
# ## コンテナ内にDBファイルが作成された
%%bash
sudo docker exec sql17cu16 ls -la /var/opt/mssql/data

#%% [markdown]
# ## ホストボリュームからもDBファイルが確認できる
%%bash
ls -la ~/SQL_Server_Container/DataVolume/data | grep DevDB

#%% [markdown]
# ## コンテナ停止してもホストボリューム上のDBファイルは消えない
%%bash
sudo docker stop sql17cu16
sudo docker ps -a --filter name=sql17cu16
ls -la ~/SQL_Server_Container/DataVolume/data | grep DevDB

#%% [markdown]
# ## コンテナ破棄してもホストボリューム上のDBファイルは消えない
%%bash
sudo docker rm -f sql17cu16
sudo docker ps -a --filter name=sql17cu16
ls -la ~/SQL_Server_Container/DataVolume/data | grep DevDB


#%% [markdown]
# # Demo 2: Docker コンテナ内での操作
# ## SQL Server 2017コンテナ起動
%%bash
sudo docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=P@ssw0rd' -p 11433:1433 -v ~/SQL_Server_Container/DataVolume:/var/opt/mssql --name sql17cu16 -d mcr.microsoft.com/mssql/server:2017-CU16
sudo docker ps -a --filter name=sql17cu16

#%% [markdown]
# ## コンテナ接続
# sudo docker exec -it sql17cu16 /bin/bash
# ## コンテナ内でmssql-cliインストール
# > apt-get update
# > apt-get install mssql-cli
# ![](image/2019-10-08-23-26-04.png)
# > which mssql-cli
# > mssql-cli -S localhost -U sa -P P@ssw0rd
# ![](image/2019-10-08-23-29-40.png)

#%% [markdown]
# ## ホスト側にはmssql-cliは存在しない
# /usr/bin/mssql-cli
# ![](image/2019-10-08-23-36-07.png)

#%% [markdown]
# ## コンテナ破棄
%%bash
sudo docker rm -f sql17cu16
sudo docker ps -a --filter name=sql17cu16

#%% [markdown]
# # Demo 3: SQL Server コンテナ内のUpgrade（2017->2019）
# ## SQL Server2019イメージは事前にPull済み
%%bash
sudo docker image list | grep 2019-RC1

#%% [markdown]
# ## SQL Server2019コンテナ起動（SQL Server 2017で作成したデータファイルをマウント）
%%bash
sudo docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=P@ssw0rd' -p 11433:1433 -v ~/SQL_Server_Container/DataVolume:/var/opt/mssql --name sql19rc1 -d mcr.microsoft.com/mssql/server:2019-RC1
sudo docker ps -a --filter name=sql19rc1

#%% [markdown]
# ## SQL Server に接続すると”Upgrade中だから待て”のエラー
# ### Sqlcmd: Error: Microsoft ODBC Driver 17 for SQL Server : Login failed for user 'sa'. Reason: Server is in script upgrade mode. Only administrator can connect at this time..
%%bash
sudo docker exec sql19rc1 /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P P@ssw0rd -Q 'select @@version'

#%% [markdown]
# ## アップグレードが終われば接続できるようになる
# ### Microsoft SQL Server 2019 (RC1) - 15.0.1900.25 (X64)
%%bash
sudo docker exec sql19rc1 /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P P@ssw0rd -Q 'select @@version'

#%% [markdown]
# ## SQL Server 2017から2019にアップグレードしたDBをSELECT
%%bash
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'use DevDB; select * from tab01'

#%% [markdown]
# # Demo 4: SQL Server コンテナ内のDBバックアップ
# ## フルバックアップ
%%bash
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'backup database DevDB to disk="/tmp/DevDB.bak" with format'
sudo docker exec sql19rc1 ls -la /tmp/DevDB.bak

#%% [markdown]
# ## バックアップをホストにコピー
%%bash
sudo docker cp sql19rc1:/tmp/DevDB.bak ~/SQL_Server_Container/DevDB.bak
ls -la ~/SQL_Server_Container/DevDB.bak

#%% [markdown]
# ## DB削除＆DBファイル削除
%%bash
sudo docker rm -f sql19rc1
sudo docker ps -a --filter name=sql19rc1
sudo rm -r ~/SQL_Server_Container/DataVolume/*

#%% [markdown]
# # Demo 5: SQL Server カスタムコンテナイメージの作成と配布
# ## Dockerfile編集
%%bash
cd ~/SQL_Server_Container
touch Dockerfile
echo 'FROM mcr.microsoft.com/mssql/server:2019-RC1' >> Dockerfile
echo 'COPY ./DevDB.bak /tmp/DevDB.bak' >> Dockerfile
echo 'CMD ["/opt/mssql/bin/sqlservr"]' >> Dockerfile
cat Dockerfile

#%% [markdown]
# ## カスタムコンテナイメージのビルド
%%bash
cd ~/SQL_Server_Container
sudo docker build -t localhost:5000/mssql/devdb:v1 .
sudo docker history localhost:5000/mssql/devdb:v1
sudo docker image list | grep devdb

#%% [markdown]
# ## ローカルプライベートレジストリ起動
%%bash
sudo docker run -d -p 5000:5000 --name registry -v ~/SQL_Server_Container/RegistryVolume:/var/lib/registry registry

#%% [markdown]
# ## ローカルプライベートレジストリにプッシュ（事前プッシュ済みなので早い）
%%bash
sudo docker push localhost:5000/mssql/devdb:v1

#%% [markdown]
# ## ローカルプライベートレジストリ確認
%%bash
wget http://localhost:5000/v2/_catalog -q -O /dev/stdout
wget http://localhost:5000/v2/mssql/devdb/tags/list -q -O /dev/stdout

#%% [markdown]
# ## ローカルに作成したカスタムコンテナイメージを削除（明示的にプライベートレジストリからPULLするため）
%%bash
sudo docker rmi localhost:5000/mssql/devdb:v1
sudo docker image list

#%% [markdown]
# ## ローカルプライベートレジストリから Pull & Run
%%bash
sudo docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=P@ssw0rd' -p 11433:1433 -v ~/SQL_Server_Container/DataVolume:/var/opt/mssql --name sql19rc1 -d localhost:5000/mssql/devdb:v1
sudo docker ps -a --filter name=sql19rc1
sudo docker image list | grep devdb

#%% [markdown]
# ## カスタム（バックアップファイルを配置）を確認
%%bash
sudo docker exec sql19rc1 ls -l /tmp

#%% [markdown]
# # Demo 6: SQL Server カスタムコンテナへのDBリストア
# ## SELECT（リストア前）
%%bash
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'use DevDB; select * from tab01'

#%% [markdown]
# ## リストア
%%bash
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'RESTORE DATABASE [DevDB] FROM DISK = "/tmp/DevDB.bak"'

#%% [markdown]
# ## SELECT
%%bash
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'use DevDB; select * from tab01'



• AutoTuning


#%%
