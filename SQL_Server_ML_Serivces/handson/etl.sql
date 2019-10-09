USE [master]
GO
CREATE LOGIN [<�}�V����>\SQLRUserGroup] FROM WINDOWS WITH DEFAULT_DATABASE=[master]
GO

USE [sql17mlhandson]
GO
CREATE USER [<�}�V����>\SQLRUserGroup] FOR LOGIN [<�}�V����>\SQLRUserGroup]
GO

EXEC columnstore_demo
GO

CREATE CLUSTERED COLUMNSTORE INDEX ColumnstoreIndex ON Table_with_5M_rows
-- DROP INDEX ColumnstoreIndex ON Table_with_5M_rows
GO

EXEC columnstore_demo
GO
