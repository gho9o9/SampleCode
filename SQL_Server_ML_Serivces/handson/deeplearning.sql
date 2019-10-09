
-- ===================================================
-- ■ STEP 0. 前準備
-- ===================================================

-- Pythonパッケージのインストール
-- cd "C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\PYTHON_SERVICES\Scripts"
-- pip install keras
-- pip install tensorflow
-- (*) GPUを使用する場合は tensorflow-gpu のインストールに加えて、CUDAとcuDNNのインストールが必要
--  cuda 8.0.61  https://developer.nvidia.com/cuda-80-ga2-download-archive
--  cudnn 5.1  https://developer.nvidia.com/cudnn
--    Download cuDNN v5.1 (Jan 20, 2017), for CUDA 8.0
--      cuDNN v5.1 Library for Windows 10
--        解凍して、CUDAフォルダ内の「bin」「include」「lib」をC:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v8.0\　以下に貼り付け（上書き）

-- ===================================================
-- ■ STEP 1. ITエンジニアあるある
-- ===================================================
USE sql17mlhandson
-- TRUNCATE TABLE models
-- TRUNCATE TABLE work

SELECT* FROM HumanCharacteristics

-- 「間違えてデータ消しちゃった...」
UPDATE HumanCharacteristics SET ["X0被験者情報_性別"] = NULL
  WHERE ID in (SELECT TOP 45 PERCENT ID FROM HumanCharacteristics ORDER BY NEWID())

SELECT* FROM HumanCharacteristics

-- 何件消えちゃったの？
SELECT count(*) AS [消しちゃった...] FROM HumanCharacteristics WHERE ["X0被験者情報_性別"] IS NULL
SELECT count(*) AS [消えずに残った] FROM HumanCharacteristics WHERE ["X0被験者情報_性別"] IS NOT NULL

-- ===================================================
-- ■ STEP 2. モデルを開発
-- ===================================================
SELECT * FROM models

DECLARE @model VARBINARY(MAX);
EXEC proc_train @model OUTPUT;
INSERT INTO models (name, model) VALUES('demo', @model);

SELECT * FROM models

-- ===================================================
-- ■ STEP 3. モデルを使って消してしまったデータを復元
-- ===================================================
SELECT * FROM work

INSERT INTO work EXEC proc_predict

SELECT * FROM work

-- ===================================================
-- ■ STEP 4. 以前のテーブルコピーを発見！（ITあるある）答え合わせしてみる
-- ===================================================
SELECT w.ID, w.[性別予測値] AS 予測した性別, h.["X0被験者情報_性別"] AS バックアップ上の性別
  FROM work w join HumanCharacteristics_backup h on w.ID = h.ID

SELECT count(*) AS [不正解の数]
  FROM work w
  join HumanCharacteristics_backup h
    on w.ID = h.ID
    AND w.性別予測値 <> h.["X0被験者情報_性別"]

