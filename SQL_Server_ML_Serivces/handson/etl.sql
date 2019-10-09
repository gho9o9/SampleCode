USE [master]
GO
CREATE LOGIN [<マシン名>\SQLRUserGroup] FROM WINDOWS WITH DEFAULT_DATABASE=[master]
GO

USE [sql17mlhandson]
GO
CREATE USER [<マシン名>\SQLRUserGroup] FOR LOGIN [<マシン名>\SQLRUserGroup]
GO

EXEC columnstore_demo
GO

CREATE CLUSTERED COLUMNSTORE INDEX ColumnstoreIndex ON Table_with_5M_rows
-- DROP INDEX ColumnstoreIndex ON Table_with_5M_rows
GO

EXEC columnstore_demo
GO
