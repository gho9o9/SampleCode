restore database demodb from disk = '/tmp/WideWorldImporters-Full.bak' with
move 'WWI_Primary' to '/var/opt/mssql/data/WideWorldImporters.mdf',
move 'WWI_UserData' to '/var/opt/mssql/data/WideWorldImporters_UserData.ndf',
move 'WWI_Log' to '/var/opt/mssql/data/WideWorldImporters.ldf',
move 'WWI_InMemory_Data_1' to '/var/opt/mssql/data/WideWorldImporters_InMemory_Data_1',
stats=5
go