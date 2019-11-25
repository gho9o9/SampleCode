
#%% [markdown]
# # 1. FCI用のnamespace作成
%%bash
kubectl create namespace mssql-fci

#%% [markdown]
# # 2. FCI用のsecret作成
%%bash
kubectl create secret generic mssql --from-literal=SA_PASSWORD=$PASSWORD -n mssql-fci

#%% [markdown]
# # 3. PVC作成
%%bash
cat ~/Jupyter/SQL_Server_on_K8s/FCI/pvc.yaml
#%%
%%bash
kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/FCI/pvc.yaml -n mssql-fci

#%% [markdown]
# # 4. Pod作成
%%bash
cat ~/Jupyter/SQL_Server_on_K8s/FCI/sql19deployment.yaml
#%%
%%bash
kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/FCI/sql19deployment.yaml -n mssql-fci

# %%
