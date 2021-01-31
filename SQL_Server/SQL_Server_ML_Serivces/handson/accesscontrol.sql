------------------------------------------------------------------------
-- �Ǘ��҂Ŏ��s�FPython/R�v���V�[�W����` �� �f���p��ʃ��[�U�̍쐬
------------------------------------------------------------------------
USE [sql17mlhandson]
GO

DROP PROCEDURE IF EXISTS access_control_demo
GO

CREATE PROCEDURE access_control_demo AS
BEGIN
EXEC sp_execute_external_script
@language = N'Python'
, @script = N'print (''Python/R�v���V�[�W���̎��s������Q�Ƃɂ̓A�N�Z�X�����K�v�ł�'')'
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
-- �Ǘ��҂Ŏ��s�FPython/R�v���V�[�W���̎��s�Ǝ����Q�Ɓi��������j
------------------------------------------------------------------------
USE [sql17mlhandson]
GO

-- Python/R�v���V�[�W���̎��s
EXEC access_control_demo
GO

-- �����̎Q�Ɓi���@�P�j
EXEC sp_helptext 'access_control_demo';
GO

-- �����̎Q�Ɓi���@�Q�j
SELECT definition FROM sys.sql_modules
WHERE object_id = OBJECT_ID('access_control_demo');
GO

------------------------------------------------------------------------
-- ��ʃ��[�U�Ŏ��s�FPython/R�v���V�[�W���̎��s�Ǝ����Q�Ɓi���s����j
------------------------------------------------------------------------
USE [sql17mlhandson]
GO
EXECUTE AS USER = 'public_user'
GO

-- Python/R�v���V�[�W���̎��s
EXEC access_control_demo
GO

-- �����̎Q�Ɓi���@�P�j
EXEC sp_helptext 'access_control_demo';
GO

-- �����̎Q�Ɓi���@�Q�j
SELECT definition FROM sys.sql_modules
WHERE object_id = OBJECT_ID('access_control_demo');
GO

-- ERROR

------------------------------------------------------------------------
-- �Ǘ��҂Ŏ��s�F������t�^
------------------------------------------------------------------------
USE [sql17mlhandson] 
GO
REVERT
GO

-- �v���V�[�W�����s���t�^
GRANT EXECUTE ON access_control_demo TO [public_user]
-- REVOKE EXECUTE ON access_control_demo FROM [public_user]

-- �O���X�N���v�g�iPython/R�j���s���t�^
GRANT EXECUTE ANY EXTERNAL SCRIPT TO [public_user]
-- REVOKE EXECUTE ANY EXTERNAL SCRIPT FROM [public_user]
 
-- ��`�Q�ƌ��t�^
GRANT VIEW DEFINITION TO [public_user]
-- REVOKE VIEW DEFINITION FROM [public_user]

------------------------------------------------------------------------
-- ��ʃ��[�U�Ŏ��s�FPython/R�v���V�[�W�����s�Ǝ����Q�Ɓi��������j
------------------------------------------------------------------------
USE [sql17mlhandson]
GO
EXECUTE AS USER = 'public_user'
GO

-- Python/R�v���V�[�W���̎��s
EXEC access_control_demo
GO

-- �����̎Q�Ɓi���@�P�j
EXEC sp_helptext 'access_control_demo';
GO

-- �����̎Q�Ɓi���@�Q�j
SELECT definition FROM sys.sql_modules
WHERE object_id = OBJECT_ID('access_control_demo');
GO

REVERT
GO

-- SUCCESS


