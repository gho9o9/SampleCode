EXEC sp_execute_external_script
@language = N'Python'
, @script = N'print (''Hello Python !'')'
GO

EXEC sp_execute_external_script
@language = N'R'
, @script = N'print (''Hello R !'')'
GO

