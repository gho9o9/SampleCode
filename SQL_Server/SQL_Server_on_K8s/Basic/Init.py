
#%% [markdown]
# # 1. コンテンツ準備 on Mac
# mkdir -p ~/OneDrive/Tech/Sample/Public/SampleCode/SQL_Server_on_K8s/Basic/RegistryVolume
# cd ~/OneDrive/Tech/Sample/Public/SampleCode/SQL_Server_on_K8s/Basic
# git clone https://github.com/ToruMakabe/Understanding-K8s.git
# cd ~/OneDrive/Tech/Sample/Public/SampleCode/SQL_Server_on_K8s/Basic/Understanding-K8s/chap03
# cp tutorial-deployment.yaml deployment.yaml
# emacs deployment.yaml
# <imageをAzureレジストリ（o9o9acr.azurecr.io/photo-view:v1.0）もしくは自作ローカルレジストリのパス(localhost:5000/webapp/photoview:v1.0)に書き換える>
# cp tutorial-service.yaml service.yaml

#%% [markdown]
# # 2. コンテンツ最新化 on Mac
# rsync -a --stats --progress ~/OneDrive/Tech/Sample/Public/SampleCode/SQL_Server_on_K8s user@host:/home/o9o9/Jupyter/
# cd ~/OneDrive/Tech/Sample/Public/SampleCode/SQL_Server_on_K8s
# git add .
# git commit -m "commit"
# git push origin master

#%% [markdown]
# # 3. デモ用コンテナイメージビルド
cd ~/Jupyter/SQL_Server_on_K8s/Basic/Understanding-K8s/chap02
sudo docker build -t localhost:5000/webapp/photoview:v1.0 v1.0/
sudo docker build -t localhost:5000/webapp/photoview:v2.0 v2.0/
sudo docker image list | grep photoview

#%% [markdown]
# # 4. プライベートレジストリの構築
%%bash
sudo docker rm -f registry
sudo docker run -d -p 5000:5000 --name registry -v ~/Jupyter/SQL_Server_on_K8s/Basic/RegistryVolume:/var/lib/registry registry
sudo docker ps -a --filter name=registry
sleep 5

#%% [markdown]
# # 5. プライベートレジストリの設定
# k8sクラスタからプライベートレジストリへのアクセス許可
#  - FW設定
#  - レジストリへの通信は既定でHTTPS。サーバ側をHTTPS対応するか、クライアント側でHTTP通信を許可
#    http://docs.docker.jp/engine/reference/commandline/pull.html
#    Docker はレジストリとの通信に https プロトコルを使います。ただし、レジストリが安全ではない接続（insecure connection）を許可している場合は除外します。詳細は 安全ではないレジストリ をご覧ください。

#%% [markdown]
# # 6.イメージのPUSH
%%bash
sudo docker push localhost:5000/webapp/photoview:v1.0
sudo docker push localhost:5000/webapp/photoview:v2.0
wget http://localhost:5000/v2/_catalog -q -O /dev/stdout
wget http://localhost:5000/v2/webapp/photoview/tags/list -q -O /dev/stdout

#%% [markdown]
# # 7. デモ用Namespace作成
%%bash
kubectl create namespace basic-k8s

# %%
