------------------------------------------------------------------------
-- 管理者で実行：Python/Rプロシージャ定義 ＆ デモ用一般ユーザの作成
------------------------------------------------------------------------
USE [sql17mlhandson]
GO

DROP PROCEDURE IF EXISTS access_control_demo
GO

CREATE PROCEDURE access_control_demo AS
BEGIN
EXEC sp_execute_external_script
@language = N'Python'
, @script = N'print (''Python/Rプロシージャの実行や実装参照にはアクセス権が必要です'')'
END 
GO

USE [master]
GO

CREATE LOGIN [public_user] WITH PASSWORD=N'public_user', DEFAULT_DATABASE=[master], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO

USE [sql17mlhandson]
GO

CREATE USER [public_user] FOR LOGIN [public_user]
GO


------------------------------------------------------------------------
-- 管理者で実行：Python/Rプロシージャの実行と実装参照（成功する）
------------------------------------------------------------------------
USE [sql17mlhandson]
GO

-- Python/Rプロシージャの実行
EXEC access_control_demo
GO

-- 実装の参照（方法１）
EXEC sp_helptext 'access_control_demo';
GO

-- 実装の参照（方法２）
SELECT definition FROM sys.sql_modules
WHERE object_id = OBJECT_ID('access_control_demo');
GO

------------------------------------------------------------------------
-- 一般ユーザで実行：Python/Rプロシージャの実行と実装参照（失敗する）
------------------------------------------------------------------------
USE [sql17mlhandson]
GO
EXECUTE AS USER = 'public_user'
GO

-- Python/Rプロシージャの実行
EXEC access_control_demo
GO

-- 実装の参照（方法１）
EXEC sp_helptext 'access_control_demo';
GO

-- 実装の参照（方法２）
SELECT definition FROM sys.sql_modules
WHERE object_id = OBJECT_ID('access_control_demo');
GO

-- ERROR

------------------------------------------------------------------------
-- 管理者で実行：権限を付与
------------------------------------------------------------------------
USE [sql17mlhandson] 
GO
REVERT
GO

-- プロシージャ実行権付与
GRANT EXECUTE ON access_control_demo TO [public_user]
-- REVOKE EXECUTE ON access_control_demo FROM [public_user]

-- 外部スクリプト（Python/R）実行権付与
GRANT EXECUTE ANY EXTERNAL SCRIPT TO [public_user]
-- REVOKE EXECUTE ANY EXTERNAL SCRIPT FROM [public_user]
 
-- 定義参照権付与
GRANT VIEW DEFINITION TO [public_user]
-- REVOKE VIEW DEFINITION FROM [public_user]

------------------------------------------------------------------------
-- 一般ユーザで実行：Python/Rプロシージャ実行と実装参照（成功する）
------------------------------------------------------------------------
USE [sql17mlhandson]
GO
EXECUTE AS USER = 'public_user'
GO

-- Python/Rプロシージャの実行
EXEC access_control_demo
GO

-- 実装の参照（方法１）
EXEC sp_helptext 'access_control_demo';
GO

-- 実装の参照（方法２）
SELECT definition FROM sys.sql_modules
WHERE object_id = OBJECT_ID('access_control_demo');
GO

REVERT
GO

-- SUCCESS


