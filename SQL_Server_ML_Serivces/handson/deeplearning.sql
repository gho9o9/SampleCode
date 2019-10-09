
-- ===================================================
-- �� STEP 0. �O����
-- ===================================================

-- Python�p�b�P�[�W�̃C���X�g�[��
-- cd "C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\PYTHON_SERVICES\Scripts"
-- pip install keras
-- pip install tensorflow
-- (*) GPU���g�p����ꍇ�� tensorflow-gpu �̃C���X�g�[���ɉ����āACUDA��cuDNN�̃C���X�g�[�����K�v
--  cuda 8.0.61  https://developer.nvidia.com/cuda-80-ga2-download-archive
--  cudnn 5.1  https://developer.nvidia.com/cudnn
--    Download cuDNN v5.1 (Jan 20, 2017), for CUDA 8.0
--      cuDNN v5.1 Library for Windows 10
--        �𓀂��āACUDA�t�H���_���́ubin�v�uinclude�v�ulib�v��C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v8.0\�@�ȉ��ɓ\��t���i�㏑���j

-- ===================================================
-- �� STEP 1. IT�G���W�j�A���邠��
-- ===================================================
USE sql17mlhandson
-- TRUNCATE TABLE models
-- TRUNCATE TABLE work

SELECT* FROM HumanCharacteristics

-- �u�ԈႦ�ăf�[�^�����������...�v
UPDATE HumanCharacteristics SET ["X0�팱�ҏ��_����"] = NULL
  WHERE ID in (SELECT TOP 45 PERCENT ID FROM HumanCharacteristics ORDER BY NEWID())

SELECT* FROM HumanCharacteristics

-- ����������������́H
SELECT count(*) AS [�����������...] FROM HumanCharacteristics WHERE ["X0�팱�ҏ��_����"] IS NULL
SELECT count(*) AS [�������Ɏc����] FROM HumanCharacteristics WHERE ["X0�팱�ҏ��_����"] IS NOT NULL

-- ===================================================
-- �� STEP 2. ���f�����J��
-- ===================================================
SELECT * FROM models

DECLARE @model VARBINARY(MAX);
EXEC proc_train @model OUTPUT;
INSERT INTO models (name, model) VALUES('demo', @model);

SELECT * FROM models

-- ===================================================
-- �� STEP 3. ���f�����g���ď����Ă��܂����f�[�^�𕜌�
-- ===================================================
SELECT * FROM work

INSERT INTO work EXEC proc_predict

SELECT * FROM work

-- ===================================================
-- �� STEP 4. �ȑO�̃e�[�u���R�s�[�𔭌��I�iIT���邠��j�������킹���Ă݂�
-- ===================================================
SELECT w.ID, w.[���ʗ\���l] AS �\����������, h.["X0�팱�ҏ��_����"] AS �o�b�N�A�b�v��̐���
  FROM work w join HumanCharacteristics_backup h on w.ID = h.ID

SELECT count(*) AS [�s�����̐�]
  FROM work w
  join HumanCharacteristics_backup h
    on w.ID = h.ID
    AND w.���ʗ\���l <> h.["X0�팱�ҏ��_����"]

