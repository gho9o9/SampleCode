
# # 4. FCI用のnamespaceとsecret作成
kubectl create namespace mssql-fci
kubectl create secret generic mssql --from-literal=SA_PASSWORD=$PASSWORD -n mssql-fci

# # 5. AG用のnamespaceとsecret作成
⭐️

#%% [markdown]
# # 6. SQL Server 2019 Big Data Cluster 作成
%%bash
azdata bdc create --accept-eula yes