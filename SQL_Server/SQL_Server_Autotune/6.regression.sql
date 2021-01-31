use demodb
go
DBCC FREEPROCCACHE
go
DECLARE @packagetypeid INT = 1;
EXEC [report] @packagetypeid;
go 

/*exec regression
go
*/