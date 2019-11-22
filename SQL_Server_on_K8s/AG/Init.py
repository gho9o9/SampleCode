#%% [markdown]
# # AG用のnamespaceとsecret作成
# ## namespace 作成
%%bash
kubectl create namespace mssql-ag(1.operator.yaml内で定義)

#%% [markdown]
# ## Secret作成
%%bash
kubectl create secret generic sql-secrets --from-literal=sapassword=$PASSWORD --from-literal=masterkeypassword=$PASSWORD -n mssql-ag

# %%
