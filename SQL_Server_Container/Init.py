
#%% [markdown]
# # 1.Demo環境事前準備
# ## 1-1.作業Dir作成
%%bash
mkdir -p ~/SQL_Server_Container
mkdir -p ~/SQL_Server_Container/DataVolume
mkdir -p ~/SQL_Server_Container/RegistryVolume

#%% [markdown]
# ## 1-2.イメージPULL
%%bash
sudo docker pull mcr.microsoft.com/mssql/server:2019-RC1
sudo docker pull mcr.microsoft.com/mssql/server:2017-CU16
sudo docker pull registry:latest
sudo docker image list

#%% [markdown]
# ## 1-3.カスタム SQL Server コンテナイメージ作成
# ### 1-3-1.コンテナ起動
%%bash
sudo docker run -e ACCEPT_EULA=Y -e MSSQL_SA_PASSWORD=$PASSWORD -p 11433:1433 -v ~/SQL_Server_Container/DataVolume:/var/opt/mssql --name sql19rc1 -d mcr.microsoft.com/mssql/server:2019-RC1
sleep 30

#%% [markdown]
# ### 1-3-2.バックアップファイル作成
# #### 1-3-2-1.DB作成
%%bash
sqlcmd -S localhost,11433 -U sa -P $PASSWORD -Q 'create database DevDB'

#%% [markdown]
# #### 1-3-2-2.データ投入
%%bash
sqlcmd -S localhost,11433 -U sa -P $PASSWORD -Q 'use DevDB; create table tab01(id int, name varchar(max)); insert into tab01 values (1, "SQL Server runs on Docker!")'
#%load_ext sql
#%sql mssql+pyodbc://sa:$PASSWORD@localhost,11433/master?DRIVER={ODBC+Driver+17+for+SQL+Server}
#%sql use DevDB; create table tab01(id int, name varchar(max)); insert into tab01 values (1, "SQL Server runs on Docker!")

#%% [markdown]
# #### 1-3-2-3.バックアップ
%%bash
sqlcmd -S localhost,11433 -U sa -P $PASSWORD -Q 'backup database DevDB to disk="/tmp/DevDB.bak" with format'
sudo docker cp sql19rc1:/tmp/DevDB.bak ~/SQL_Server_Container/DevDB.bak
ls -la ~/SQL_Server_Container

#%% [markdown]
# #### 1-3-2-4.クリーンアップ
%%bash
sudo docker rm -f sql19rc1
sudo rm -r ~/SQL_Server_Container/DataVolume/*

#%% [markdown]
# ### 1-3-3.Dockerfile作成
%%bash
cd ~/SQL_Server_Container
touch Dockerfile
echo 'FROM mcr.microsoft.com/mssql/server:2019-RC1' >> Dockerfile
echo 'COPY ./DevDB.bak /tmp/DevDB.bak' >> Dockerfile
echo 'CMD ["/opt/mssql/bin/sqlservr"]' >> Dockerfile
cat Dockerfile

#%% [markdown]
# ### 1-3-4.カスタムイメージのビルド
%%bash
cd ~/SQL_Server_Container
sudo docker build -t localhost:5000/mssql/devdb:v1 .
sudo docker image list | grep devdb
sudo docker history localhost:5000/mssql/devdb:v1

#%% [markdown]
# ### 1-3-5.ローカルプライベートレジストリの構築
%%bash
sudo docker run -d -p 5000:5000 --name registry -v ~/SQL_Server_Container/RegistryVolume:/var/lib/registry registry
sudo docker ps -a --filter name=registry
sleep 5

#%% [markdown]
# ### 1-3-6.イメージのPUSH
%%bash
sudo docker push localhost:5000/mssql/devdb:v1
sudo docker rm -f registry
# sudo rm -r ~/SQL_Server_Container/DataVolume/*

#%% [markdown]
# ## 1-2.AutoTuneデモ用コンテナ準備
# ### 1-2-1.コンテナ作成 
%%bash
sudo docker run -e ACCEPT_EULA=Y -e MSSQL_SA_PASSWORD=$PASSWORD -p 61433:1433 --name sqlautotune -d mcr.microsoft.com/mssql/server:2019-RC1
sudo docker ps -a --filter name=sqlautotune

#%% [markdown]
# ### 1-2-2.テストデータダウンロード
%%bash
# sudo docker exec sqlautotune wget https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak -o /tmp/WideWorldImporters-Full.bak
curl -L -o /tmp/WideWorldImporters-Full.bak 'https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak'
sudo docker cp /tmp/WideWorldImporters-Full.bak sqlautotune:/tmp/WideWorldImporters-Full.bak
rm /tmp/WideWorldImporters-Full.bak

#%% [markdown]
# ### 1-2-3.デモ用クエリダウンロード
%%bash
cd ~/SQL_Server_Container
# apt instal subversion
# sudo rm -rf ~/SQL_Server_Container/SQL_Server_Autotune
svn export --force https://github.com/gho9o9/SampleCode/trunk/SQL_Server_Autotune

#%% [markdown]
# ### 1-2-4.テストデータリストア
%%bash
sqlcmd -S localhost,61433 -U sa -P $PASSWORD \
  -i ~/SQL_Server_Container/SQL_Server_Autotune/0.restorewwi_linux.sql
sqlcmd -S localhost,61433 -U sa -P $PASSWORD \
  -Q 'select name from sys.databases'
# sudo docker exec sqlautotune /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $PASSWORD -Q "RESTORE DATABASE [demodb] FROM DISK = N'/tmp/WideWorldImporters-Full.bak' WITH MOVE 'WWI_Primary' TO '/var/opt/mssql/data/WideWorldImporters.mdf', MOVE 'WWI_UserData' TO '/var/opt/mssql/data/WideWorldImporters_UserData.ndf', MOVE 'WWI_Log' TO '/var/opt/mssql/data/WideWorldImporters.ldf', MOVE 'WWI_InMemory_Data_1' TO '/var/opt/mssql/data/WideWorldImporters_InMemory_Data_1', FILE = 1, NOUNLOAD, REPLACE, STATS = 5"
# sudo docker exec sqlautotune /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $PASSWORD -Q 'select name from sys.databases'

#%% [markdown]
# ### 1-2-5.デモ用プロシージャ定義
%%bash
sqlcmd -S localhost,61433 -U sa -P $PASSWORD \
  -i ~/SQL_Server_Container/SQL_Server_Autotune/1.setup.sql

