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
# # 1. 事前に準備済みのK8s環境を確認
#%%
%%bash
az aks show -g rg_bdc -n o9o9aks
#%%
%%bash
az vm list -g MC_RG_BDC_O9O9AKS_JAPANEAST -d
#%%
%%bash
kubectl get node -o wide


#%% [markdown]
# # 2. シンプルデモ（エンジンエックス）
# ![](image/2019-12-03-12-54-07.png)

#%% [markdown]
# ## 2−1. namespace作成
%%bash
kubectl create namespace hello-k8s

#%% [markdown]
# ## 2−2. Pod作成(nginxコンテナを含んだPodを３冗長で作成しラベルmyappをつける)
%%bash
kubectl run myapp --image=nginx:1.17 --replicas 3 --labels="app=myapp" -n hello-k8s
#%%
%%bash
kubectl get pod -o wide -n hello-k8s

#%% [markdown]
# ## 2−3. Service作成（ホストポート80番で受けてラベルmyappに転送するロードバランサを作成）
%%bash
kubectl create service loadbalancer --tcp 80:80 myapp -n hello-k8s
#%%
%%bash
kubectl get service myapp -n hello-k8s

#%% [markdown]
# ## 2−4. サービスにアクセス
# http://[EXTERNAL-IP]
# ![](image/2019-12-03-13-29-19.png)

#%% [markdown]
# ## 2−5. namespace削除
%%bash
kubectl delete namespace hello-k8s


#%% [markdown]
# # 3. マニュフェストによるリソース作成

#%% [markdown]
# # 3−1. デモ用Namespace作成
%%bash
kubectl create namespace basic-k8s

#%% [markdown]
# # 3−2. Pod作成
# ![](image/2019-12-03-13-05-35.png)
#%%
%%bash
kubectl get pod -o wide -n basic-k8s
#%%
%%bash
cat ~/Jupyter/SQL_Server_on_K8s/Basic/Understanding-K8s/chap03/deployment.yaml
#%%
%%bash
kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/Basic/Understanding-K8s/chap03/deployment.yaml -n basic-k8s
#%%
%%bash
kubectl get pod -o wide -n basic-k8s
#%% [markdown]
# ![](image/2019-12-03-13-06-57.png)


#%% [markdown]
# # 3−3. Service作成
%%bash
cat ~/Jupyter/SQL_Server_on_K8s/Basic/Understanding-K8s/chap03/service.yaml
#%%
%%bash
kubectl apply -f ~/Jupyter/SQL_Server_on_K8s/Basic/Understanding-K8s/chap03/service.yaml -n basic-k8s
#%%
%%bash
kubectl get service -o wide -n basic-k8s
#%% [markdown]
# ![](image/2019-12-03-13-07-50.png)


#%% [markdown]
# # 3−4. サービスにアクセス
# http://[EXTERNAL-IP]
# ![](image/2019-12-03-13-08-54.png)
# ![](image/2019-12-03-13-36-16.png)


#%% [markdown]
# # 3−5. Pod擬似障害
%%bash
kubectl delete pod photoview-deployment-5b6f5dbdf-6jrx4 -n basic-k8s
#%%
%%bash
kubectl get pod -o wide -n basic-k8s


#%% [markdown]
# # 3−6. 環境破棄
%%bash
kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/Basic/Understanding-K8s/chap03/service.yaml -n basic-k8s
kubectl delete -f ~/Jupyter/SQL_Server_on_K8s/Basic/Understanding-K8s/chap03/deployment.yaml -n basic-k8s
#%% [markdown]
# ![](image/2019-12-03-13-05-35.png)


#%% [markdown]
# # TODO. Deployment

#%% [markdown]
# ![](image/2019-11-24-22-12-50.png)
