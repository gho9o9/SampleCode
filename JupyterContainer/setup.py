#%%
%%bash
uname -a
cat /etc/lsb-release
cat /etc/odbcinst.ini

#%%
import pyodbc 
print(pyodbc.drivers())
%load_ext sql

#%%
# 参考
#mssql+pyodbc://user:password@server/database?DRIVER={enty in /etc/odbcinst.ini}'
%sql mssql+pyodbc://o9o9:P@ssw0rd@o9o9mssql.database.windows.net/master?DRIVER={/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.4.so.1.1}
#%sql mssql+pyodbc://o9o9:P@ssw0rd@o9o9mssql.database.windows.net/master?DRIVER={ODBC Driver 17 for SQL Server}
%sql select @@version

#%%
# 参考
server = 'o9o9mssql.database.windows.net' 
database = 'master' 
username = 'o9o9' 
password = 'P@ssw0rd' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0]) 
    row = cursor.fetchone()
cursor.close()
cnxn.close()

#%%[markdown]
#fooをprint

#%%
print('foo')

#%%[markdown]
## barをecho

#%%
%%bash
echo bar

#%%[markdown]
# # Markdown h1
# ## Markdown h2
# ### Markdown h3
# - Markdown 1
# - Markdown 2
# - Markdown 3
# # Image
# ![](image/2019-09-29-01-47-54.png)
# [タイトル][1]
# [1]:https://qiita.com/h1na/items/d305d49b5a27e92d132a
#%%
