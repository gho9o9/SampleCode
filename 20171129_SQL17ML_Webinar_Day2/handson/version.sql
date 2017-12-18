SELECT @@VERSION AS "SQL Server Version"

EXEC sp_execute_external_script
       @language = N'Python'
       , @script = N'
import sys
import pkg_resources
OutputDataSet = pandas.DataFrame(
    {"property_name": ["Python VERSION", "Python HOME", "Python LIBRARY_PATH", "RevoScalePy VERSION"],
    "property_value": [sys.version, sys.executable[:-10], str(sys.path), pkg_resources.get_distribution("revoscalepy").version]}
  )
'
WITH result SETS ((Name nvarchar(100), Value nvarchar(4000)));

EXEC sp_execute_external_script
       @language = N'R'
       , @script = N'
OutputDataSet <- data.frame(
  property_name = c("R VERSION", "R HOME", "R LIBRARY_PATH", "RevoScaleR VERSION"), 
  property_value = c(R.Version()$version.string, R.home(), .libPaths(), Revo.version$version.string),
  stringsAsFactors = FALSE)
'
WITH RESULT SETS ((Name nvarchar(100), Value nvarchar(4000)));
