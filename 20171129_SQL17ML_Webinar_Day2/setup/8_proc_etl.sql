DROP TABLE IF EXISTS Table_with_5M_rows
GO
WITH a AS (SELECT * FROM (VALUES(1),(2),(3),(4),(5),(6),(7),(8),(9),(10)) AS a(a))
SELECT TOP(5000000)
ROW_NUMBER() OVER (ORDER BY a.a) AS OrderItemId
,a.a + b.a + c.a + d.a + e.a + f.a + g.a + h.a AS OrderId
,a.a * 10 AS Price
,CONCAT(a.a, N' ', b.a, N' ', c.a, N' ', d.a, N' ', e.a, N' ', f.a, N' ', g.a, N' ', h.a) AS ProductName
INTO Table_with_5M_rows
FROM a, a AS b, a AS c, a AS d, a AS e, a AS f, a AS g, a AS h;
GO

DROP PROCEDURE IF EXISTS columnstore_demo
GO
CREATE PROCEDURE columnstore_demo AS
BEGIN
  EXEC sp_execute_external_script  
    @language = N'Python'  
    , @script = N'
import pyodbc
from datetime import datetime
cnxn = pyodbc.connect(''DRIVER={ODBC Driver 13 for SQL Server};SERVER=.;DATABASE=sql17mlhandson;Trusted_Connection=yes;'')
cursor = cnxn.cursor()
tsql = "SELECT SUM(Price) as sum FROM Table_with_5M_rows"
a = datetime.now()
with cursor.execute(tsql):
  b = datetime.now()
  c = b - a
  for row in cursor:
    print (''Sum:'', str(row[0]))
  print (''QueryTime:'', c.microseconds, ''micro sec'')
'
END 
GO
