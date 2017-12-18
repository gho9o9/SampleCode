CREATE PROCEDURE MyProc(@input varchar(10), @output int OUTPUT) AS
BEGIN
  EXEC sp_execute_external_script
    @language = N'Python', 
    @script = N'
print(''Hello '' + InputParam)
MyOutput = MyInput
OutputParam  = len(MyOutput)
print(OutputParam)', 
    @input_data_1 = N'SELECT 1, 2, 3;', 
    @input_data_1_name = N'MyInput', 
    @output_data_1_name = N'MyOutput', 
    @params = N'@InputParam varchar(10), @OutputParam int OUTPUT', 
    @InputParam = @input, @OutputParam = @output OUTPUT
    WITH RESULT SETS (( C1 int, C2 int, C3 int ));
END
GO

DECLARE @NumOfRec int
EXEC MyProc @input='Python!', @output=@NumOfRec OUTPUT
SELECT @NumOfRec as NumOfRec
GO
