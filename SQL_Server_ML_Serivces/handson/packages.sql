
EXECUTE sp_execute_external_script  
@language=N'Python'  
,@script = N'
import pkg_resources
for dist in pkg_resources.working_set:
    print(dist.project_name, dist.version)'

EXECUTE sp_execute_external_script  
@language=N'R'  
,@script = N'str(OutputDataSet);  
packagematrix <- installed.packages();
print(packagematrix[,c("Package", "Version")])'
