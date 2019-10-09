
#%% [markdown]
# # Demo環境事前準備
# ## 作業Dir作成
%%bash
mkdir -p ~/SQL_Server_Container
mkdir -p ~/SQL_Server_Container/DataVolume
mkdir -p ~/SQL_Server_Container/RegistryVolume

#%% [markdown]
# ## イメージPULL
%%bash
sudo docker image list
sudo docker pull mcr.microsoft.com/mssql/server:2019-RC1
sudo docker pull mcr.microsoft.com/mssql/server:2017-CU16
sudo docker pull registry:latest

#%% [markdown]
# ## カスタム SQL Server コンテナイメージ作成
# ### バックアップファイル作成
%%bash
sudo docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=P@ssw0rd' -p 11433:1433 -v ~/SQL_Server_Container/DataVolume:/var/opt/mssql --name sql19rc1 -d mcr.microsoft.com/mssql/server:2019-RC1
sleep 30
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'create database DevDB'
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'use DevDB; create table tab01(id int, name varchar(max)); insert into tab01 values (1, "SQL Server runs on Docker!")'
sqlcmd -S localhost,11433 -U sa -P P@ssw0rd -Q 'backup database DevDB to disk="/tmp/DevDB.bak" with format'
sudo docker cp sql19rc1:/tmp/DevDB.bak ~/SQL_Server_Container/DevDB.bak
ls -la ~/SQL_Server_Container
sudo docker rm -f sql19rc1
sudo rm -r ~/SQL_Server_Container/DataVolume/*

#%% [markdown]
# ### Dockerfile作成
%%bash
cd ~/SQL_Server_Container
touch Dockerfile
echo 'FROM mcr.microsoft.com/mssql/server:2019-RC1' >> Dockerfile
echo 'COPY ./DevDB.bak /tmp/DevDB.bak' >> Dockerfile
echo 'CMD ["/opt/mssql/bin/sqlservr"]' >> Dockerfile
cat Dockerfile

#%% [markdown]
# ### カスタムイメージのビルド
%%bash
cd ~/SQL_Server_Container
sudo docker build -t localhost:5000/mssql/devdb:v1 .
sudo docker image list | grep devdb
sudo docker history localhost:5000/mssql/devdb:v1

#%% [markdown]
# ### ローカルプライベートレジストリの構築とPUSH
%%bash
sudo docker run -d -p 5000:5000 --name registry -v ~/SQL_Server_Container/RegistryVolume:/var/lib/registry registry
sudo docker ps -a --filter name=registry
sudo docker push localhost:5000/mssql/devdb:v1
sudo docker rm -f registry
# sudo rm -r ~/SQL_Server_Container/DataVolume/*

#%% [markdown]
# ## AutoTuneデモ用コンテナ準備
# ### コンテナ作成 
%%bash
sudo docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=P@ssw0rd' -p 61433:1433 --name sqlautotune -d mcr.microsoft.com/mssql/server:2019-latest
sudo docker ps -a --filter name=sqlautotune

#%% [markdown]
# ### テストデータダウンロード
%%bash
# sudo docker exec sqlautotune wget https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak -o /tmp/WideWorldImporters-Full.bak
curl -L -o /tmp/WideWorldImporters-Full.bak 'https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak'
sudo docker cp /tmp/WideWorldImporters-Full.bak sqlautotune:/tmp/WideWorldImporters-Full.bak
rm /tmp/WideWorldImporters-Full.bak

#%% [markdown]
# ### テストデータリストア
%%bash
sudo docker exec sqlautotune /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P P@ssw0rd -Q "RESTORE DATABASE [WideWorldImporters-Full] FROM DISK = N'/tmp/WideWorldImporters-Full.bak' WITH MOVE 'WWI_Primary' TO '/var/opt/mssql/data/WideWorldImporters.mdf', MOVE 'WWI_UserData' TO '/var/opt/mssql/data/WideWorldImporters_UserData.ndf', MOVE 'WWI_Log' TO '/var/opt/mssql/data/WideWorldImporters.ldf', MOVE 'WWI_InMemory_Data_1' TO '/var/opt/mssql/data/WideWorldImporters_InMemory_Data_1', FILE = 1, NOUNLOAD, REPLACE, STATS = 5"
sudo docker exec sqlautotune /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P P@ssw0rd -Q 'select name from sys.databases'
