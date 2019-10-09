CREATE TABLE models( name nchar(10), model varbinary(max) )
CREATE TABLE work (ID int, [���ʗ\���l] int)

update HumanCharacteristics set ["X0�팱�ҏ��_����"] = 1 where ["X0�팱�ҏ��_����"] = '"�j��"'
update HumanCharacteristics set ["X0�팱�ҏ��_����"] = 0 where ["X0�팱�ҏ��_����"] = '"����"'

ALTER TABLE HumanCharacteristics ADD [ID] [int] IDENTITY(1,1) NOT NULL ;

ALTER TABLE HumanCharacteristics ADD  CONSTRAINT [PK_ID] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO

BEGIN TRANSACTION
SET QUOTED_IDENTIFIER ON
SET ARITHABORT ON
SET NUMERIC_ROUNDABORT OFF
SET CONCAT_NULL_YIELDS_NULL ON
SET ANSI_NULLS ON
SET ANSI_PADDING ON
SET ANSI_WARNINGS ON
COMMIT
BEGIN TRANSACTION
GO
CREATE TABLE dbo.Tmp_HumanCharacteristics
	(
	ID int NOT NULL IDENTITY (1, 1),
	["X0�팱�ҏ��_����"] varchar(50) NULL,
	["X0�팱�ҏ��_�N��"] varchar(50) NULL,
	["X0�팱�ҏ��_�g��  mm "] varchar(50) NULL,
	["X0�팱�ҏ��_�̏d  kg "] varchar(50) NULL,
	["X1�g�̐��@_�̎��b    "] varchar(50) NULL,
	["X1�g�̐��@_BMI"] varchar(50) NULL,
	["X1�g�̐��@_�z�ō�  mm "] varchar(50) NULL,
	["X1�g�̐��@_����  mm "] varchar(50) NULL,
	["X1�g�̐��@_�I����  mm "] varchar(50) NULL,
	["X1�g�̐��@_�]�q��  mm "] varchar(50) NULL,
	["X1�g�̐��@_�����㉏��  mm "] varchar(50) NULL,
	["X1�g�̐��@_���ʒ[��  mm "] varchar(50) NULL,
	["X1�g�̐��@_���z����  mm "] varchar(50) NULL,
	["X1�g�̐��@_��r��  mm "] varchar(50) NULL,
	["X1�g�̐��@_�O�r��  mm "] varchar(50) NULL,
	["X1�g�̐��@_��ڒ�  mm "] varchar(50) NULL,
	["X1�g�̐��@_���ڒ�  mm "] varchar(50) NULL,
	["X1�g�̐��@_����  mm "] varchar(50) NULL,
	["X1�g�̐��@_�z��  mm "] varchar(50) NULL,
	["X1�g�̐��@_�㕔����  mm "] varchar(50) NULL,
	["X1�g�̐��@_����  mm "] varchar(50) NULL,
	["X1�g�̐��@_��r��  mm "] varchar(50) NULL,
	["X1�g�̐��@_�O�r�ő��  mm "] varchar(50) NULL,
	["X1�g�̐��@_��ڈ�  mm "] varchar(50) NULL,
	["X1�g�̐��@_���ڍő��  mm "] varchar(50) NULL,
	["X1�g�̐��@_�蒷  mm "] varchar(50) NULL,
	["X1�g�̐��@_���w��  mm "] varchar(50) NULL,
	["X1�g�̐��@_���  mm "] varchar(50) NULL,
	["X1�g�̐��@_�蕝  mm "] varchar(50) NULL,
	["X1�g�̐��@_���w�߈ʊ֐ߕ�  mm "] varchar(50) NULL,
	["X1�g�̐��@_���w���ʊ֐ߕ�  mm "] varchar(50) NULL,
	["X1�g�̐��@_��� ��܎w��[�ԍő勗��  mm "] varchar(50) NULL,
	["X1�g�̐��@_������a  mm "] varchar(50) NULL,
	["X2�̗͑���_����  N "] varchar(50) NULL,
	["X2�̗͑���_�����̑O��  cm "] varchar(50) NULL,
	["X2�̗͑���_��̋N����  �� "] varchar(50) NULL,
	["X2�̗͑���_�S�g��������  msec "] varchar(50) NULL,
	["X2�̗͑���_��Б���������  sec "] varchar(50) NULL,
	["X2�̗͑���_��������  cm "] varchar(50) NULL,
	["X3�֐߉���_��֐� ����  deg "] varchar(50) NULL,
	["X3�֐߉���_��֐� �L�W  deg "] varchar(50) NULL,
	["X3�֐߉���_�I�֐� ����  deg "] varchar(50) NULL,
	["X3�֐߉���_�I�֐� �L�W  deg "] varchar(50) NULL,
	["X3�֐߉���_���֐� ����  deg "] varchar(50) NULL,
	["X3�֐߉���_���֐� �L�W  deg "] varchar(50) NULL,
	["X3�֐߉���_���֐� �����L�W  deg "] varchar(50) NULL,
	["X3�֐߉���_���֐� ��������  deg "] varchar(50) NULL,
	["X3�֐߉���_���֐� ����  deg "] varchar(50) NULL,
	["X3�֐߉���_���֐� �L�W  deg "] varchar(50) NULL,
	["X3�֐߉���_�G�֐� ����  deg "] varchar(50) NULL,
	["X3�֐߉���_�G�֐� �L�W  deg "] varchar(50) NULL,
	["X3�֐߉���_�Ҋ֐� ����  deg "] varchar(50) NULL,
	["X3�֐߉���_�Ҋ֐� �L�W  deg "] varchar(50) NULL,
	["X5�I�v�V����_TUG  sec "] varchar(50) NULL,
	["X5�I�v�V����_�N��������  sec "] varchar(50) NULL,
	["X5�I�v�V����_���[�`����  cm "] varchar(50) NULL,
	["X5�I�v�V����_�J�� �W���΍�  ���E    mm "] varchar(50) NULL,
	["X5�I�v�V����_�J�� �W���΍�   �O��    mm "] varchar(50) NULL,
	["X5�I�v�V����_�J�� �ő�U��  ���E    mm "] varchar(50) NULL,
	["X5�I�v�V����_�J�� �ő�U��  �O��    mm "] varchar(50) NULL,
	["X5�I�v�V����_�J�� ���O�Ւ�   mm "] varchar(50) NULL,
	["X5�I�v�V����_�� �W���΍�  ���E   mm "] varchar(50) NULL,
	["X5�I�v�V����_�� �W���΍�   �O��   mm "] varchar(50) NULL,
	["X5�I�v�V����_�� �ő�U��  ���E   mm "] varchar(50) NULL,
	["X5�I�v�V����_�� �ő�U��  �O��   mm "] varchar(50) NULL,
	["X5�I�v�V����_�� ���O�Ւ�  mm "] varchar(50) NULL,
	["X5�I�v�V����_2�_�Ԏ��ʋ��� ��   mm "] varchar(50) NULL,
	["X5�I�v�V����_2�_�Ԏ��ʋ��� �d�w��  mm "] varchar(50) NULL,
	["X5�I�v�V����_2�_�Ԏ��ʋ��� ���w��  mm "] varchar(50) NULL,
	["X5�I�v�V����_2�_�Ԏ��ʋ��� �d�w  mm "] varchar(50) NULL,
	["X6�㎈�����_���� ��� �I��������   N "] varchar(50) NULL,
	["X6�㎈�����_���� ���� �����Ȋp�x135    N "] varchar(50) NULL,
	["X6�㎈�����_����  ��� �I��������   N "] varchar(50) NULL,
	["X6�㎈�����_����  ���� �����Ȋp�x135    N "] varchar(50) NULL,
	["X6�㎈�����_�� ���Ԃ����� �E��   Nm "] varchar(50) NULL,
	["X6�㎈�����_�� ���Ԃ����� ����   Nm "] varchar(50) NULL,
	["X6�㎈�����_�� �͂��݈��� �E��   Nm "] varchar(50) NULL,
	["X6�㎈�����_�� �͂��݈��� ����   Nm "] varchar(50) NULL,
	["X6�㎈�����_�㎈��� �E��  Nm "] varchar(50) NULL,
	["X6�㎈�����_�㎈��� ����  Nm "] varchar(50) NULL,
	["X6�㎈�����_�܂� �e�w ���w����  Nm "] varchar(50) NULL,
	["X6�㎈�����_�܂� �e�w ���w  Nm "] varchar(50) NULL,
	["X6�㎈�����_�܂� �e�w  ���w ���w   Nm "] varchar(50) NULL,
	["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _01"] varchar(50) NULL,
	["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _02"] varchar(50) NULL,
	["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _03"] varchar(50) NULL,
	["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _04"] varchar(50) NULL,
	["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _05"] varchar(50) NULL,
	["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _06"] varchar(50) NULL,
	["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _07"] varchar(50) NULL
	)  ON [PRIMARY]
GO
ALTER TABLE dbo.Tmp_HumanCharacteristics SET (LOCK_ESCALATION = TABLE)
GO
SET IDENTITY_INSERT dbo.Tmp_HumanCharacteristics ON
GO
IF EXISTS(SELECT * FROM dbo.HumanCharacteristics)
	 EXEC('INSERT INTO dbo.Tmp_HumanCharacteristics (ID, ["X0�팱�ҏ��_����"], ["X0�팱�ҏ��_�N��"], ["X0�팱�ҏ��_�g��  mm "], ["X0�팱�ҏ��_�̏d  kg "], ["X1�g�̐��@_�̎��b    "], ["X1�g�̐��@_BMI"], ["X1�g�̐��@_�z�ō�  mm "], ["X1�g�̐��@_����  mm "], ["X1�g�̐��@_�I����  mm "], ["X1�g�̐��@_�]�q��  mm "], ["X1�g�̐��@_�����㉏��  mm "], ["X1�g�̐��@_���ʒ[��  mm "], ["X1�g�̐��@_���z����  mm "], ["X1�g�̐��@_��r��  mm "], ["X1�g�̐��@_�O�r��  mm "], ["X1�g�̐��@_��ڒ�  mm "], ["X1�g�̐��@_���ڒ�  mm "], ["X1�g�̐��@_����  mm "], ["X1�g�̐��@_�z��  mm "], ["X1�g�̐��@_�㕔����  mm "], ["X1�g�̐��@_����  mm "], ["X1�g�̐��@_��r��  mm "], ["X1�g�̐��@_�O�r�ő��  mm "], ["X1�g�̐��@_��ڈ�  mm "], ["X1�g�̐��@_���ڍő��  mm "], ["X1�g�̐��@_�蒷  mm "], ["X1�g�̐��@_���w��  mm "], ["X1�g�̐��@_���  mm "], ["X1�g�̐��@_�蕝  mm "], ["X1�g�̐��@_���w�߈ʊ֐ߕ�  mm "], ["X1�g�̐��@_���w���ʊ֐ߕ�  mm "], ["X1�g�̐��@_��� ��܎w��[�ԍő勗��  mm "], ["X1�g�̐��@_������a  mm "], ["X2�̗͑���_����  N "], ["X2�̗͑���_�����̑O��  cm "], ["X2�̗͑���_��̋N����  �� "], ["X2�̗͑���_�S�g��������  msec "], ["X2�̗͑���_��Б���������  sec "], ["X2�̗͑���_��������  cm "], ["X3�֐߉���_��֐� ����  deg "], ["X3�֐߉���_��֐� �L�W  deg "], ["X3�֐߉���_�I�֐� ����  deg "], ["X3�֐߉���_�I�֐� �L�W  deg "], ["X3�֐߉���_���֐� ����  deg "], ["X3�֐߉���_���֐� �L�W  deg "], ["X3�֐߉���_���֐� �����L�W  deg "], ["X3�֐߉���_���֐� ��������  deg "], ["X3�֐߉���_���֐� ����  deg "], ["X3�֐߉���_���֐� �L�W  deg "], ["X3�֐߉���_�G�֐� ����  deg "], ["X3�֐߉���_�G�֐� �L�W  deg "], ["X3�֐߉���_�Ҋ֐� ����  deg "], ["X3�֐߉���_�Ҋ֐� �L�W  deg "], ["X5�I�v�V����_TUG  sec "], ["X5�I�v�V����_�N��������  sec "], ["X5�I�v�V����_���[�`����  cm "], ["X5�I�v�V����_�J�� �W���΍�  ���E    mm "], ["X5�I�v�V����_�J�� �W���΍�   �O��    mm "], ["X5�I�v�V����_�J�� �ő�U��  ���E    mm "], ["X5�I�v�V����_�J�� �ő�U��  �O��    mm "], ["X5�I�v�V����_�J�� ���O�Ւ�   mm "], ["X5�I�v�V����_�� �W���΍�  ���E   mm "], ["X5�I�v�V����_�� �W���΍�   �O��   mm "], ["X5�I�v�V����_�� �ő�U��  ���E   mm "], ["X5�I�v�V����_�� �ő�U��  �O��   mm "], ["X5�I�v�V����_�� ���O�Ւ�  mm "], ["X5�I�v�V����_2�_�Ԏ��ʋ��� ��   mm "], ["X5�I�v�V����_2�_�Ԏ��ʋ��� �d�w��  mm "], ["X5�I�v�V����_2�_�Ԏ��ʋ��� ���w��  mm "], ["X5�I�v�V����_2�_�Ԏ��ʋ��� �d�w  mm "], ["X6�㎈�����_���� ��� �I��������   N "], ["X6�㎈�����_���� ���� �����Ȋp�x135    N "], ["X6�㎈�����_����  ��� �I��������   N "], ["X6�㎈�����_����  ���� �����Ȋp�x135    N "], ["X6�㎈�����_�� ���Ԃ����� �E��   Nm "], ["X6�㎈�����_�� ���Ԃ����� ����   Nm "], ["X6�㎈�����_�� �͂��݈��� �E��   Nm "], ["X6�㎈�����_�� �͂��݈��� ����   Nm "], ["X6�㎈�����_�㎈��� �E��  Nm "], ["X6�㎈�����_�㎈��� ����  Nm "], ["X6�㎈�����_�܂� �e�w ���w����  Nm "], ["X6�㎈�����_�܂� �e�w ���w  Nm "], ["X6�㎈�����_�܂� �e�w  ���w ���w   Nm "], ["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _01"], ["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _02"], ["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _03"], ["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _04"], ["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _05"], ["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _06"], ["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _07"])
		SELECT ID, ["X0�팱�ҏ��_����"], ["X0�팱�ҏ��_�N��"], ["X0�팱�ҏ��_�g��  mm "], ["X0�팱�ҏ��_�̏d  kg "], ["X1�g�̐��@_�̎��b    "], ["X1�g�̐��@_BMI"], ["X1�g�̐��@_�z�ō�  mm "], ["X1�g�̐��@_����  mm "], ["X1�g�̐��@_�I����  mm "], ["X1�g�̐��@_�]�q��  mm "], ["X1�g�̐��@_�����㉏��  mm "], ["X1�g�̐��@_���ʒ[��  mm "], ["X1�g�̐��@_���z����  mm "], ["X1�g�̐��@_��r��  mm "], ["X1�g�̐��@_�O�r��  mm "], ["X1�g�̐��@_��ڒ�  mm "], ["X1�g�̐��@_���ڒ�  mm "], ["X1�g�̐��@_����  mm "], ["X1�g�̐��@_�z��  mm "], ["X1�g�̐��@_�㕔����  mm "], ["X1�g�̐��@_����  mm "], ["X1�g�̐��@_��r��  mm "], ["X1�g�̐��@_�O�r�ő��  mm "], ["X1�g�̐��@_��ڈ�  mm "], ["X1�g�̐��@_���ڍő��  mm "], ["X1�g�̐��@_�蒷  mm "], ["X1�g�̐��@_���w��  mm "], ["X1�g�̐��@_���  mm "], ["X1�g�̐��@_�蕝  mm "], ["X1�g�̐��@_���w�߈ʊ֐ߕ�  mm "], ["X1�g�̐��@_���w���ʊ֐ߕ�  mm "], ["X1�g�̐��@_��� ��܎w��[�ԍő勗��  mm "], ["X1�g�̐��@_������a  mm "], ["X2�̗͑���_����  N "], ["X2�̗͑���_�����̑O��  cm "], ["X2�̗͑���_��̋N����  �� "], ["X2�̗͑���_�S�g��������  msec "], ["X2�̗͑���_��Б���������  sec "], ["X2�̗͑���_��������  cm "], ["X3�֐߉���_��֐� ����  deg "], ["X3�֐߉���_��֐� �L�W  deg "], ["X3�֐߉���_�I�֐� ����  deg "], ["X3�֐߉���_�I�֐� �L�W  deg "], ["X3�֐߉���_���֐� ����  deg "], ["X3�֐߉���_���֐� �L�W  deg "], ["X3�֐߉���_���֐� �����L�W  deg "], ["X3�֐߉���_���֐� ��������  deg "], ["X3�֐߉���_���֐� ����  deg "], ["X3�֐߉���_���֐� �L�W  deg "], ["X3�֐߉���_�G�֐� ����  deg "], ["X3�֐߉���_�G�֐� �L�W  deg "], ["X3�֐߉���_�Ҋ֐� ����  deg "], ["X3�֐߉���_�Ҋ֐� �L�W  deg "], ["X5�I�v�V����_TUG  sec "], ["X5�I�v�V����_�N��������  sec "], ["X5�I�v�V����_���[�`����  cm "], ["X5�I�v�V����_�J�� �W���΍�  ���E    mm "], ["X5�I�v�V����_�J�� �W���΍�   �O��    mm "], ["X5�I�v�V����_�J�� �ő�U��  ���E    mm "], ["X5�I�v�V����_�J�� �ő�U��  �O��    mm "], ["X5�I�v�V����_�J�� ���O�Ւ�   mm "], ["X5�I�v�V����_�� �W���΍�  ���E   mm "], ["X5�I�v�V����_�� �W���΍�   �O��   mm "], ["X5�I�v�V����_�� �ő�U��  ���E   mm "], ["X5�I�v�V����_�� �ő�U��  �O��   mm "], ["X5�I�v�V����_�� ���O�Ւ�  mm "], ["X5�I�v�V����_2�_�Ԏ��ʋ��� ��   mm "], ["X5�I�v�V����_2�_�Ԏ��ʋ��� �d�w��  mm "], ["X5�I�v�V����_2�_�Ԏ��ʋ��� ���w��  mm "], ["X5�I�v�V����_2�_�Ԏ��ʋ��� �d�w  mm "], ["X6�㎈�����_���� ��� �I��������   N "], ["X6�㎈�����_���� ���� �����Ȋp�x135    N "], ["X6�㎈�����_����  ��� �I��������   N "], ["X6�㎈�����_����  ���� �����Ȋp�x135    N "], ["X6�㎈�����_�� ���Ԃ����� �E��   Nm "], ["X6�㎈�����_�� ���Ԃ����� ����   Nm "], ["X6�㎈�����_�� �͂��݈��� �E��   Nm "], ["X6�㎈�����_�� �͂��݈��� ����   Nm "], ["X6�㎈�����_�㎈��� �E��  Nm "], ["X6�㎈�����_�㎈��� ����  Nm "], ["X6�㎈�����_�܂� �e�w ���w����  Nm "], ["X6�㎈�����_�܂� �e�w ���w  Nm "], ["X6�㎈�����_�܂� �e�w  ���w ���w   Nm "], ["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _01"], ["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _02"], ["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _03"], ["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _04"], ["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _05"], ["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _06"], ["X7�A���P�[�g_���i�ʋ΂┃�����ŕ����Ă��邩�ǂ��� _07"] FROM dbo.HumanCharacteristics WITH (HOLDLOCK TABLOCKX)')
GO
SET IDENTITY_INSERT dbo.Tmp_HumanCharacteristics OFF
GO
DROP TABLE dbo.HumanCharacteristics
GO
EXECUTE sp_rename N'dbo.Tmp_HumanCharacteristics', N'HumanCharacteristics', 'OBJECT' 
GO
ALTER TABLE dbo.HumanCharacteristics ADD CONSTRAINT
	PK_ID PRIMARY KEY CLUSTERED 
	(
	ID
	) WITH( STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

GO
COMMIT
