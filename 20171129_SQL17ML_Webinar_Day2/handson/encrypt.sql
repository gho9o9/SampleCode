-- “ï“Ç‰»
DROP PROCEDURE IF EXISTS non_encrypted_demo
GO
CREATE PROCEDURE non_encrypted_demo AS
BEGIN
EXEC sp_execute_external_script
@language = N'Python'
, @script = N'print (''‚±‚ÌPythonŽÀ‘•‚Í“ï“Ç‰»‚µ‚Ä‚¢‚Ü‚¹‚ñ'')'
END 
GO

EXEC non_encrypted_demo
GO

EXEC sp_helptext 'non_encrypted_demo';
GO

SELECT definition AS "Non-Encrypted Proc Definition" FROM sys.sql_modules
WHERE object_id = OBJECT_ID('non_encrypted_demo');
GO



DROP PROCEDURE IF EXISTS encrypted_demo
GO
CREATE PROCEDURE encrypted_demo WITH ENCRYPTION AS
BEGIN
EXEC sp_execute_external_script
@language = N'Python'
, @script = N'print (''‚±‚ÌPythonŽÀ‘•‚Í“ï“Ç‰»‚µ‚Ä‚¢‚Ü‚·'')'
END 
GO

EXEC encrypted_demo
GO

EXEC sp_helptext 'encrypted_demo';
GO

SELECT definition AS "Encrypted Proc Definition" FROM sys.sql_modules
WHERE object_id = OBJECT_ID('encrypted_demo');
GO