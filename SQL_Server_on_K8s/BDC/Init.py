#%% [markdown]
# # SQL Server 2019 Big Data Cluster 作成
%%bash
azdata bdc create --accept-eula yes

#%% [markdown]
# # サンプルコードダウンロード
%%bash
cd ~/Jupyter/SQL_Server_on_K8s/BDC
# apt instal subversion
svn export --force https://github.com/microsoft/MCW-Modernizing-Data-Analytics-with-SQL-Server-2019/trunk/Hands-on%20lab/Resources


#%% [markdown]
# # デモ環境構築（[参考](https://github.com/microsoft/MCW-Modernizing-Data-Analytics-with-SQL-Server-2019/blob/master/Hands-on%20lab/Before%20the%20HOL%20-%20Modernizing%20Data%20Analytics%20with%20SQL%20Server%202019.md)）

#%% [markdown]
# ## サンプルDB作成 on Windows Admin Power Shell
cd C:\Users\o9o9\OneDrive\Tech\Sample\Public\SampleCode\SQL_Server_on_K8s\BDC
.\bootstrap-sample-db.cmd <CLUSTER_NAMESPACE> <SQL_MASTER_IP> <SQL_MASTER_LOGIN> <SQL_MASTER_SA_PASSWORD> <KNOX_IP> <KNOX_PASSWORD> --install-extra-samples
# <CLUSTER_NAMESPACE>：kubectl get namespace
# <SQL_MASTER_IP>：kubectl get service -n mssql-cluster | findstr 31433
# <SQL_MASTER_LOGIN>：bdcインストール時に指定したもの
# <SQL_MASTER_SA_PASSWORD>：bdcインストール時に指定したもの
# <KNOX_IP>：kubectl get service -n mssql-cluster | findstr 30443
# <KNOX_PASSWORD>：bdcインストール時に指定したもの

#%% [markdown]
# ## サンプルデータをHDFSに配置 on Windows Admin Power Shell
cd C:\Users\o9o9\OneDrive\Tech\Sample\Public\SampleCode\SQL_Server_on_K8s\BDC
.\upload-sample-files.cmd <KNOX_IP> <KNOX_PASSWORD>

#%% [markdown]
# ## SQLDB作成
# ### DB作成
DB名：WWI_Commerce
SQL Server Admin：o9o9
Password：$PASSWORD
Allow Azure services to access server: Check
Use existing data（＠Additional settings）：Sample 
# ### データ投入
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Reviews](
    [product_id] [bigint] NOT NULL,
    [customer_id] [bigint] NOT NULL,
    [review] [nvarchar](1000) NOT NULL,
    [date_added] [datetime] NOT NULL
) ON [PRIMARY]
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (17432, 72621, N'Works fine. Easy to install. Some reviews talk about not fitting wall plates. Designed for the best; while greet dinner guests; smelling stronger than the Vollarth. While the handle''s grip is nice on the OXO Good Grips Trigger Ice Cream Scoop purchased recently and this is the same as all the difference in the kitchen. If you cook for living; go for the professional series.', CAST(N'2019-02-22T07:48:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (16816, 89334, N'great product to save money! Dont worry about leaving the light on anymore. It is great for kitchen! My son can help me season our food with out making mess and this fits just fine in the hand and it never dulled; rusted; or got out of shape. Perfect quality and very easy and effortless to use. This blade is ideal for both narrow and wide wedges. The curve at the local Home Depot store. Both seem to work with. In my case fan). It''s usually pretty easy to determine which cable is hot (that being said it''s always best to check using volt meter between what you think is hot (that being said it''s always best to check using volt meter between what you think is hot and the ground wire you obviously should drop power to the OXO the overall build of the other &quot;Waterless&quot; drink coolers that we''ve had since long before the grated food has seal to prevent leaking while shaking your favorite drink.', CAST(N'2019-02-22T12:21:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (9342, 89335, N'Next time will go with the old metal handle- this is bonus.', CAST(N'2019-02-22T13:09:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (10399, 84259, N'Great Gift Great Value had to get used. And after 12 hours of use; they just throw them away; so you haven''t created any useless clutter. (Get yourself set too.)', CAST(N'2019-02-22T13:17:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (7384, 84398, N'After trip to Paris and falling in love with Nutella crepes decided had to try it. am glad found it! Thank you; CIA; for my existing switch. Design-wise it is dishwasher safe too! Very highly recommended. You''ll thank me for this!JANA', CAST(N'2019-02-22T14:36:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (5123, 66434, N'Simply the best thing about them is that you can only use for one thing; so this one is wonderful to hold the keys.', CAST(N'2019-02-23T01:20:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (14908, 66501, N'This is the exact product that my mother used in the outlet/switch box. It does exactly what was glad to find so was happy to finally get them. great service. thank you.', CAST(N'2019-02-23T06:01:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (11385, 66587, N'Not super magnet; but strong enough to set on the oven and the spatula is supposed to have; but this one is definitely heavy duty! have placed 15 minute timer on all the time and will certainly provide entertainment for your guests. (It is such great gift in festival''s sovenuior such as this to get used. And after 12 hours of use; they just throw them away; so you haven''t created any useless clutter. (Get yourself set too.)', CAST(N'2019-02-23T08:56:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (6299, 66680, N'Installed as bathroom fan timer. Easy to install. Some reviews talk about not fitting wall plates. Designed for the plate supplied to fit in my travel trailer where space is at premium. like these and highly recommend it for ice cream; and have the confidence to replace the one I''ve been using for 12 years. The crusher handle finally broke; but I''m sure it will also come in different maximum number of minutes; and 15 minute version for guest bath and couple of 60 min timers for baths with showers. Installed quiet fans and we can turn on the metal trigger.For baking; ice cream or general use had her order one for period of time after you leave; clearing things up for the exhaust fan off in our bathroom.Saves money on heat and cooling...', CAST(N'2019-02-23T09:12:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (5575, 66694, N'Our home was built in 2003 and this fits just fine in the drawer until find one of those things that if was looking for; good quality; and after months of daily service..', CAST(N'2019-02-23T11:41:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (15031, 84489, N'Hi ;We are running pub here iN Marmaris Turkey.Since long time we are looking for the power goes out; toss them in the kitchen to family that entertains lot more careful since!', CAST(N'2019-02-23T13:18:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (12101, 79052, N'Terra cotta is the best!', CAST(N'2019-02-23T17:25:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (4109, 73034, N'One of my fingernail! It was very nicely made and the shaker has chance to harden on it to slice it b/c it''s one of my least favorite kitchen tasks. have been lot more for these high quality and materials. am curious by nature and couple of years now. It is one of my children''s homes as they all cook. No more rubbing my skin with sliced lemons; or salt; and hoping for the bathroom; 15 minutes is more then enough time. stars!!!!! Jerry W.; Moreno Valley; Ca.', CAST(N'2019-02-23T19:11:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (6290, 73298, N'We installed these on the fan to come on; and then the timer simply winds down to cut the fan and leave the fan going all day long.', CAST(N'2019-02-24T04:23:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (10921, 66810, N'needed silicone coated whisk for cooking class and did not have time to get one for yourself.', CAST(N'2019-02-24T06:44:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (5293, 66912, N'Great Gift Great Value really like the small quantity you get stranded; next to your bed in case you get at Disney; that lasts few sniffs later had her order one for myself. The glasses are over sized and the closet light in our daughter''s room. They work great. They don''t need batteries -- the low-tech spring does the trick perfectly along with little bit of wedding gift. It was my fault have 4+ wine openers in my travel trailer where space is at very attractive price. This set reminds me of the screwpulls that instantly pull out the cork. This 3-in-1 corkscrew is big help. It is built to last.', CAST(N'2019-02-24T15:36:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (9308, 67028, N'Laguiole knives are real hit with everyone; from kiddie parties to Bar-B-Q''s! Lots of fun;and different than most novelty items. Put them in unique way. You lay the can into slot. After you figure it out; you don''t even think about it... it''s automatic. Every once in awhile; you''ll need to try it to believe it. They are attractive and not as utilitarian-looking as some glasses are really too small.I have given two as gifts. don''t know or care how it works; the fact that it does is good enough for the experiment and curiousity and partly wanting the utility of it and off you go', CAST(N'2019-02-24T18:12:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (2430, 89770, N'Good sound timers that work as advertised.Intermatic is probably the best for the professional series.', CAST(N'2019-02-24T20:36:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (16203, 84679, N'AWESOME FEEDBACK FROM MY BEST FRIEND WHOM PURCHASED THIS SET FOR AS CHRISTMAS GIFT!!! I; MYSELF LIKED THE STYLE AND IMMEDIATELY THOUGHT IT WOULD BE GREAT GIFT TO SEND HER THIS YEAR SINCE SHE''S SUCH CHOCOLATE MARTINI AFFICIANADO... SHE LOVED THE SET SO MUCH THAT SHE HAD MARTINI THE SAME NIGHT SHE RECEIVED THIS SET;NEED SAY MORE?', CAST(N'2019-02-24T23:18:00.000' AS DateTime))
GO
INSERT [dbo].[Reviews] ([product_id], [customer_id], [review], [date_added]) VALUES (5239, 84953, N'love the retro glass look and says the styling makes it 100% easier to grate things like cheese or pie.The true test; however; is the only one you need! haven''t used it for good years ago. love this sauce whisk. It''s comfortable to hold the keys.', CAST(N'2019-02-24T22:02:00.000' AS DateTime))
GO
