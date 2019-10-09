CREATE TABLE models( name nchar(10), model varbinary(max) )
CREATE TABLE work (ID int, [性別予測値] int)

update HumanCharacteristics set ["X0被験者情報_性別"] = 1 where ["X0被験者情報_性別"] = '"男性"'
update HumanCharacteristics set ["X0被験者情報_性別"] = 0 where ["X0被験者情報_性別"] = '"女性"'

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
	["X0被験者情報_性別"] varchar(50) NULL,
	["X0被験者情報_年齢"] varchar(50) NULL,
	["X0被験者情報_身長  mm "] varchar(50) NULL,
	["X0被験者情報_体重  kg "] varchar(50) NULL,
	["X1身体寸法_体脂肪    "] varchar(50) NULL,
	["X1身体寸法_BMI"] varchar(50) NULL,
	["X1身体寸法_頚椎高  mm "] varchar(50) NULL,
	["X1身体寸法_肩峰高  mm "] varchar(50) NULL,
	["X1身体寸法_肘頭高  mm "] varchar(50) NULL,
	["X1身体寸法_転子高  mm "] varchar(50) NULL,
	["X1身体寸法_脛骨上縁高  mm "] varchar(50) NULL,
	["X1身体寸法_内果端高  mm "] varchar(50) NULL,
	["X1身体寸法_頭頚部長  mm "] varchar(50) NULL,
	["X1身体寸法_上腕長  mm "] varchar(50) NULL,
	["X1身体寸法_前腕長  mm "] varchar(50) NULL,
	["X1身体寸法_大腿長  mm "] varchar(50) NULL,
	["X1身体寸法_下腿長  mm "] varchar(50) NULL,
	["X1身体寸法_足長  mm "] varchar(50) NULL,
	["X1身体寸法_頚囲  mm "] varchar(50) NULL,
	["X1身体寸法_上部胸囲  mm "] varchar(50) NULL,
	["X1身体寸法_腹囲  mm "] varchar(50) NULL,
	["X1身体寸法_上腕囲  mm "] varchar(50) NULL,
	["X1身体寸法_前腕最大囲  mm "] varchar(50) NULL,
	["X1身体寸法_大腿囲  mm "] varchar(50) NULL,
	["X1身体寸法_下腿最大囲  mm "] varchar(50) NULL,
	["X1身体寸法_手長  mm "] varchar(50) NULL,
	["X1身体寸法_第二指長  mm "] varchar(50) NULL,
	["X1身体寸法_手囲  mm "] varchar(50) NULL,
	["X1身体寸法_手幅  mm "] varchar(50) NULL,
	["X1身体寸法_第二指近位関節幅  mm "] varchar(50) NULL,
	["X1身体寸法_第二指遠位関節幅  mm "] varchar(50) NULL,
	["X1身体寸法_第一 第五指尖端間最大距離  mm "] varchar(50) NULL,
	["X1身体寸法_握り内径  mm "] varchar(50) NULL,
	["X2体力測定_握力  N "] varchar(50) NULL,
	["X2体力測定_長座体前屈  cm "] varchar(50) NULL,
	["X2体力測定_上体起こし  回 "] varchar(50) NULL,
	["X2体力測定_全身反応時間  msec "] varchar(50) NULL,
	["X2体力測定_閉眼片足立ち時間  sec "] varchar(50) NULL,
	["X2体力測定_垂直跳び  cm "] varchar(50) NULL,
	["X3関節可動域_手関節 屈曲  deg "] varchar(50) NULL,
	["X3関節可動域_手関節 伸展  deg "] varchar(50) NULL,
	["X3関節可動域_肘関節 屈曲  deg "] varchar(50) NULL,
	["X3関節可動域_肘関節 伸展  deg "] varchar(50) NULL,
	["X3関節可動域_肩関節 屈曲  deg "] varchar(50) NULL,
	["X3関節可動域_肩関節 伸展  deg "] varchar(50) NULL,
	["X3関節可動域_肩関節 水平伸展  deg "] varchar(50) NULL,
	["X3関節可動域_肩関節 水平屈曲  deg "] varchar(50) NULL,
	["X3関節可動域_足関節 屈曲  deg "] varchar(50) NULL,
	["X3関節可動域_足関節 伸展  deg "] varchar(50) NULL,
	["X3関節可動域_膝関節 屈曲  deg "] varchar(50) NULL,
	["X3関節可動域_膝関節 伸展  deg "] varchar(50) NULL,
	["X3関節可動域_股関節 屈曲  deg "] varchar(50) NULL,
	["X3関節可動域_股関節 伸展  deg "] varchar(50) NULL,
	["X5オプション_TUG  sec "] varchar(50) NULL,
	["X5オプション_起きあがり  sec "] varchar(50) NULL,
	["X5オプション_リーチ肩峰高  cm "] varchar(50) NULL,
	["X5オプション_開眼 標準偏差  左右    mm "] varchar(50) NULL,
	["X5オプション_開眼 標準偏差   前後    mm "] varchar(50) NULL,
	["X5オプション_開眼 最大振幅  左右    mm "] varchar(50) NULL,
	["X5オプション_開眼 最大振幅  前後    mm "] varchar(50) NULL,
	["X5オプション_開眼 総軌跡長   mm "] varchar(50) NULL,
	["X5オプション_閉眼 標準偏差  左右   mm "] varchar(50) NULL,
	["X5オプション_閉眼 標準偏差   前後   mm "] varchar(50) NULL,
	["X5オプション_閉眼 最大振幅  左右   mm "] varchar(50) NULL,
	["X5オプション_閉眼 最大振幅  前後   mm "] varchar(50) NULL,
	["X5オプション_閉眼 総軌跡長  mm "] varchar(50) NULL,
	["X5オプション_2点間識別距離 踵   mm "] varchar(50) NULL,
	["X5オプション_2点間識別距離 拇指球  mm "] varchar(50) NULL,
	["X5オプション_2点間識別距離 小指下  mm "] varchar(50) NULL,
	["X5オプション_2点間識別距離 拇指  mm "] varchar(50) NULL,
	["X6上肢操作力_押す 低位 肘頭下縁高   N "] varchar(50) NULL,
	["X6上肢操作力_押す 高位 肩屈曲角度135    N "] varchar(50) NULL,
	["X6上肢操作力_引く  低位 肘頭下縁高   N "] varchar(50) NULL,
	["X6上肢操作力_引く  高位 肩屈曲角度135    N "] varchar(50) NULL,
	["X6上肢操作力_回す かぶせ握り 右回し   Nm "] varchar(50) NULL,
	["X6上肢操作力_回す かぶせ握り 左回し   Nm "] varchar(50) NULL,
	["X6上肢操作力_回す はさみ握り 右回し   Nm "] varchar(50) NULL,
	["X6上肢操作力_回す はさみ握り 左回し   Nm "] varchar(50) NULL,
	["X6上肢操作力_上肢回旋 右回し  Nm "] varchar(50) NULL,
	["X6上肢操作力_上肢回旋 左回し  Nm "] varchar(50) NULL,
	["X6上肢操作力_つまむ 親指 示指側腹  Nm "] varchar(50) NULL,
	["X6上肢操作力_つまむ 親指 示指  Nm "] varchar(50) NULL,
	["X6上肢操作力_つまむ 親指  示指 中指   Nm "] varchar(50) NULL,
	["X7アンケート_普段通勤や買い物で歩いているかどうか _01"] varchar(50) NULL,
	["X7アンケート_普段通勤や買い物で歩いているかどうか _02"] varchar(50) NULL,
	["X7アンケート_普段通勤や買い物で歩いているかどうか _03"] varchar(50) NULL,
	["X7アンケート_普段通勤や買い物で歩いているかどうか _04"] varchar(50) NULL,
	["X7アンケート_普段通勤や買い物で歩いているかどうか _05"] varchar(50) NULL,
	["X7アンケート_普段通勤や買い物で歩いているかどうか _06"] varchar(50) NULL,
	["X7アンケート_普段通勤や買い物で歩いているかどうか _07"] varchar(50) NULL
	)  ON [PRIMARY]
GO
ALTER TABLE dbo.Tmp_HumanCharacteristics SET (LOCK_ESCALATION = TABLE)
GO
SET IDENTITY_INSERT dbo.Tmp_HumanCharacteristics ON
GO
IF EXISTS(SELECT * FROM dbo.HumanCharacteristics)
	 EXEC('INSERT INTO dbo.Tmp_HumanCharacteristics (ID, ["X0被験者情報_性別"], ["X0被験者情報_年齢"], ["X0被験者情報_身長  mm "], ["X0被験者情報_体重  kg "], ["X1身体寸法_体脂肪    "], ["X1身体寸法_BMI"], ["X1身体寸法_頚椎高  mm "], ["X1身体寸法_肩峰高  mm "], ["X1身体寸法_肘頭高  mm "], ["X1身体寸法_転子高  mm "], ["X1身体寸法_脛骨上縁高  mm "], ["X1身体寸法_内果端高  mm "], ["X1身体寸法_頭頚部長  mm "], ["X1身体寸法_上腕長  mm "], ["X1身体寸法_前腕長  mm "], ["X1身体寸法_大腿長  mm "], ["X1身体寸法_下腿長  mm "], ["X1身体寸法_足長  mm "], ["X1身体寸法_頚囲  mm "], ["X1身体寸法_上部胸囲  mm "], ["X1身体寸法_腹囲  mm "], ["X1身体寸法_上腕囲  mm "], ["X1身体寸法_前腕最大囲  mm "], ["X1身体寸法_大腿囲  mm "], ["X1身体寸法_下腿最大囲  mm "], ["X1身体寸法_手長  mm "], ["X1身体寸法_第二指長  mm "], ["X1身体寸法_手囲  mm "], ["X1身体寸法_手幅  mm "], ["X1身体寸法_第二指近位関節幅  mm "], ["X1身体寸法_第二指遠位関節幅  mm "], ["X1身体寸法_第一 第五指尖端間最大距離  mm "], ["X1身体寸法_握り内径  mm "], ["X2体力測定_握力  N "], ["X2体力測定_長座体前屈  cm "], ["X2体力測定_上体起こし  回 "], ["X2体力測定_全身反応時間  msec "], ["X2体力測定_閉眼片足立ち時間  sec "], ["X2体力測定_垂直跳び  cm "], ["X3関節可動域_手関節 屈曲  deg "], ["X3関節可動域_手関節 伸展  deg "], ["X3関節可動域_肘関節 屈曲  deg "], ["X3関節可動域_肘関節 伸展  deg "], ["X3関節可動域_肩関節 屈曲  deg "], ["X3関節可動域_肩関節 伸展  deg "], ["X3関節可動域_肩関節 水平伸展  deg "], ["X3関節可動域_肩関節 水平屈曲  deg "], ["X3関節可動域_足関節 屈曲  deg "], ["X3関節可動域_足関節 伸展  deg "], ["X3関節可動域_膝関節 屈曲  deg "], ["X3関節可動域_膝関節 伸展  deg "], ["X3関節可動域_股関節 屈曲  deg "], ["X3関節可動域_股関節 伸展  deg "], ["X5オプション_TUG  sec "], ["X5オプション_起きあがり  sec "], ["X5オプション_リーチ肩峰高  cm "], ["X5オプション_開眼 標準偏差  左右    mm "], ["X5オプション_開眼 標準偏差   前後    mm "], ["X5オプション_開眼 最大振幅  左右    mm "], ["X5オプション_開眼 最大振幅  前後    mm "], ["X5オプション_開眼 総軌跡長   mm "], ["X5オプション_閉眼 標準偏差  左右   mm "], ["X5オプション_閉眼 標準偏差   前後   mm "], ["X5オプション_閉眼 最大振幅  左右   mm "], ["X5オプション_閉眼 最大振幅  前後   mm "], ["X5オプション_閉眼 総軌跡長  mm "], ["X5オプション_2点間識別距離 踵   mm "], ["X5オプション_2点間識別距離 拇指球  mm "], ["X5オプション_2点間識別距離 小指下  mm "], ["X5オプション_2点間識別距離 拇指  mm "], ["X6上肢操作力_押す 低位 肘頭下縁高   N "], ["X6上肢操作力_押す 高位 肩屈曲角度135    N "], ["X6上肢操作力_引く  低位 肘頭下縁高   N "], ["X6上肢操作力_引く  高位 肩屈曲角度135    N "], ["X6上肢操作力_回す かぶせ握り 右回し   Nm "], ["X6上肢操作力_回す かぶせ握り 左回し   Nm "], ["X6上肢操作力_回す はさみ握り 右回し   Nm "], ["X6上肢操作力_回す はさみ握り 左回し   Nm "], ["X6上肢操作力_上肢回旋 右回し  Nm "], ["X6上肢操作力_上肢回旋 左回し  Nm "], ["X6上肢操作力_つまむ 親指 示指側腹  Nm "], ["X6上肢操作力_つまむ 親指 示指  Nm "], ["X6上肢操作力_つまむ 親指  示指 中指   Nm "], ["X7アンケート_普段通勤や買い物で歩いているかどうか _01"], ["X7アンケート_普段通勤や買い物で歩いているかどうか _02"], ["X7アンケート_普段通勤や買い物で歩いているかどうか _03"], ["X7アンケート_普段通勤や買い物で歩いているかどうか _04"], ["X7アンケート_普段通勤や買い物で歩いているかどうか _05"], ["X7アンケート_普段通勤や買い物で歩いているかどうか _06"], ["X7アンケート_普段通勤や買い物で歩いているかどうか _07"])
		SELECT ID, ["X0被験者情報_性別"], ["X0被験者情報_年齢"], ["X0被験者情報_身長  mm "], ["X0被験者情報_体重  kg "], ["X1身体寸法_体脂肪    "], ["X1身体寸法_BMI"], ["X1身体寸法_頚椎高  mm "], ["X1身体寸法_肩峰高  mm "], ["X1身体寸法_肘頭高  mm "], ["X1身体寸法_転子高  mm "], ["X1身体寸法_脛骨上縁高  mm "], ["X1身体寸法_内果端高  mm "], ["X1身体寸法_頭頚部長  mm "], ["X1身体寸法_上腕長  mm "], ["X1身体寸法_前腕長  mm "], ["X1身体寸法_大腿長  mm "], ["X1身体寸法_下腿長  mm "], ["X1身体寸法_足長  mm "], ["X1身体寸法_頚囲  mm "], ["X1身体寸法_上部胸囲  mm "], ["X1身体寸法_腹囲  mm "], ["X1身体寸法_上腕囲  mm "], ["X1身体寸法_前腕最大囲  mm "], ["X1身体寸法_大腿囲  mm "], ["X1身体寸法_下腿最大囲  mm "], ["X1身体寸法_手長  mm "], ["X1身体寸法_第二指長  mm "], ["X1身体寸法_手囲  mm "], ["X1身体寸法_手幅  mm "], ["X1身体寸法_第二指近位関節幅  mm "], ["X1身体寸法_第二指遠位関節幅  mm "], ["X1身体寸法_第一 第五指尖端間最大距離  mm "], ["X1身体寸法_握り内径  mm "], ["X2体力測定_握力  N "], ["X2体力測定_長座体前屈  cm "], ["X2体力測定_上体起こし  回 "], ["X2体力測定_全身反応時間  msec "], ["X2体力測定_閉眼片足立ち時間  sec "], ["X2体力測定_垂直跳び  cm "], ["X3関節可動域_手関節 屈曲  deg "], ["X3関節可動域_手関節 伸展  deg "], ["X3関節可動域_肘関節 屈曲  deg "], ["X3関節可動域_肘関節 伸展  deg "], ["X3関節可動域_肩関節 屈曲  deg "], ["X3関節可動域_肩関節 伸展  deg "], ["X3関節可動域_肩関節 水平伸展  deg "], ["X3関節可動域_肩関節 水平屈曲  deg "], ["X3関節可動域_足関節 屈曲  deg "], ["X3関節可動域_足関節 伸展  deg "], ["X3関節可動域_膝関節 屈曲  deg "], ["X3関節可動域_膝関節 伸展  deg "], ["X3関節可動域_股関節 屈曲  deg "], ["X3関節可動域_股関節 伸展  deg "], ["X5オプション_TUG  sec "], ["X5オプション_起きあがり  sec "], ["X5オプション_リーチ肩峰高  cm "], ["X5オプション_開眼 標準偏差  左右    mm "], ["X5オプション_開眼 標準偏差   前後    mm "], ["X5オプション_開眼 最大振幅  左右    mm "], ["X5オプション_開眼 最大振幅  前後    mm "], ["X5オプション_開眼 総軌跡長   mm "], ["X5オプション_閉眼 標準偏差  左右   mm "], ["X5オプション_閉眼 標準偏差   前後   mm "], ["X5オプション_閉眼 最大振幅  左右   mm "], ["X5オプション_閉眼 最大振幅  前後   mm "], ["X5オプション_閉眼 総軌跡長  mm "], ["X5オプション_2点間識別距離 踵   mm "], ["X5オプション_2点間識別距離 拇指球  mm "], ["X5オプション_2点間識別距離 小指下  mm "], ["X5オプション_2点間識別距離 拇指  mm "], ["X6上肢操作力_押す 低位 肘頭下縁高   N "], ["X6上肢操作力_押す 高位 肩屈曲角度135    N "], ["X6上肢操作力_引く  低位 肘頭下縁高   N "], ["X6上肢操作力_引く  高位 肩屈曲角度135    N "], ["X6上肢操作力_回す かぶせ握り 右回し   Nm "], ["X6上肢操作力_回す かぶせ握り 左回し   Nm "], ["X6上肢操作力_回す はさみ握り 右回し   Nm "], ["X6上肢操作力_回す はさみ握り 左回し   Nm "], ["X6上肢操作力_上肢回旋 右回し  Nm "], ["X6上肢操作力_上肢回旋 左回し  Nm "], ["X6上肢操作力_つまむ 親指 示指側腹  Nm "], ["X6上肢操作力_つまむ 親指 示指  Nm "], ["X6上肢操作力_つまむ 親指  示指 中指   Nm "], ["X7アンケート_普段通勤や買い物で歩いているかどうか _01"], ["X7アンケート_普段通勤や買い物で歩いているかどうか _02"], ["X7アンケート_普段通勤や買い物で歩いているかどうか _03"], ["X7アンケート_普段通勤や買い物で歩いているかどうか _04"], ["X7アンケート_普段通勤や買い物で歩いているかどうか _05"], ["X7アンケート_普段通勤や買い物で歩いているかどうか _06"], ["X7アンケート_普段通勤や買い物で歩いているかどうか _07"] FROM dbo.HumanCharacteristics WITH (HOLDLOCK TABLOCKX)')
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
