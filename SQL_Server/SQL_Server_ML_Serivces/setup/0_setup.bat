sqlcmd -E -d master -i ".\1_createdb.sql"
sqlcmd -E -d sql17mlhandson -i ".\2_createtable.sql"
copy /Y .\3_dataset.csv C:\3_dataset.csv
sqlcmd -E -d sql17mlhandson -i ".\3_loaddata.sql"
del C:\3_dataset.csv
sqlcmd -E -d sql17mlhandson -i ".\4_dataprep.sql"
sqlcmd -E -d sql17mlhandson -i ".\5_backup.sql"
sqlcmd -E -d sql17mlhandson -i ".\6_proc_train.sql"
sqlcmd -E -d sql17mlhandson -i ".\7_proc_predict.sql"
sqlcmd -E -d sql17mlhandson -i ".\8_proc_etl.sql"
pause