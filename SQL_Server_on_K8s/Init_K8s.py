
#%% [markdown]
# # 1.K8s作成
%%bash
az group create --resource-group rg_bdc --location japaneast
az aks create --name o9o9aks --resource-group rg_bdc --node-count 3 --kubernetes-version 1.14.6 --node-vm-size Standard_B16ms

#%% [markdown]
# # 2.クライアントに資格情報をセット
%%bash
az aks get-credentials --admin --resource-group rg_bdc --name o9o9aks

#%% [markdown]
# # 3. K8s Dashborad へのアクセス権を設定（https://docs.microsoft.com/ja-jp/azure/aks/kubernetes-dashboard）
%%bash
kubectl create clusterrolebinding kubernetes-dashboard --clusterrole=cluster-admin --serviceaccount=kube-system:kubernetes-dashboard
