
#%% [markdown]
# # Demo環境削除
%%bash
sudo docker rm -f sql19rc1
sudo docker rm -f sql17cu16
sudo docker rmi localhost:5000/mssql/devdb:v1
sudo rm -r ~/SQL_Server_Container