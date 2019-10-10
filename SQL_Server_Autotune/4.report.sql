use demodb
go
declare @packagetypeid int = 7;
exec dbo.report @packagetypeid
go 1000000