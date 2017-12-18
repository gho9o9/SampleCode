USE sql17mlhandson

DROP PROCEDURE IF EXISTS encrypted_demo
GO
CREATE PROCEDURE encrypted_demo WITH ENCRYPTION AS
BEGIN
EXEC sp_execute_external_script
@language = N'Python'
, @script = N'print (''‚±‚ÌPythonŽÀ‘•‚Í“ï“Ç‰»‚µ‚Ä‚¢‚Ü‚·'')'
END 
GO

EXEC sp_helptext 'encrypted_demo';
GO

SELECT definition AS "Encrypted Proc Definition" FROM sys.sql_modules
WHERE object_id = OBJECT_ID('encrypted_demo');
GO

-- Connect using the DAC then execute the below

DECLARE @encrypted NVARCHAR(MAX)
SET @encrypted = ( 
 SELECT imageval 
 FROM sys.sysobjvalues
 WHERE OBJECT_NAME(objid) = 'encrypted_demo' )
DECLARE @encryptedLength INT
SET @encryptedLength = DATALENGTH(@encrypted) / 2

DECLARE @procedureHeader NVARCHAR(MAX)
SET @procedureHeader = N'ALTER PROCEDURE encrypted_demo WITH ENCRYPTION AS '
SET @procedureHeader = @procedureHeader + REPLICATE(N'-',(@encryptedLength - LEN(@procedureHeader)))
EXEC sp_executesql @procedureHeader
DECLARE @blankEncrypted NVARCHAR(MAX)
SET @blankEncrypted = ( 
 SELECT imageval 
 FROM sys.sysobjvalues
 WHERE OBJECT_NAME(objid) = 'encrypted_demo' )

SET @procedureHeader = N'CREATE PROCEDURE encrypted_demo WITH ENCRYPTION AS '
SET @procedureHeader = @procedureHeader + REPLICATE(N'-',(@encryptedLength - LEN(@procedureHeader)))

DECLARE @cnt SMALLINT
DECLARE @decryptedChar NCHAR(1)
DECLARE @decryptedMessage NVARCHAR(MAX)
SET @decryptedMessage = ''
SET @cnt = 1
WHILE @cnt <> @encryptedLength
BEGIN
  SET @decryptedChar = 
      NCHAR(
        UNICODE(SUBSTRING(
           @encrypted, @cnt, 1)) ^
        UNICODE(SUBSTRING(
           @procedureHeader, @cnt, 1)) ^
        UNICODE(SUBSTRING(
           @blankEncrypted, @cnt, 1))
     )
  SET @decryptedMessage = @decryptedMessage + @decryptedChar
 SET @cnt = @cnt + 1
END
SELECT @decryptedMessage AS "Decrypted Proc Definition"