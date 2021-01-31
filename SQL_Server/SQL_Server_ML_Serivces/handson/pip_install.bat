cd "C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\PYTHON_SERVICES\Scripts"
pip freeze | findstr /c:tensorflow /c:Keras
pip install tensorflow
pip install keras
pip freeze | findstr /c:tensorflow /c:Keras
pause