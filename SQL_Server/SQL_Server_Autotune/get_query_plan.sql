USE tempdb  -- 2000互換モードのDBだとCROSS APPLYがsyntax errorになるのでtempdbに移動
SELECT TOP 100 /*mssqlstats_v2*/
  DB_NAME(MIN(dbid)) AS "DB Name"
  ,MIN(text) AS "Text"
  ,MIN(statement_text) AS "Statement Text"
  ,CONVERT(xml, MIN(whole)) AS "Whole Query Plan"  -- 全体プラン出力
  ,CONVERT(xml, MIN(part)) AS "Part Query Plan"  -- 部分プラン出力
  ,MAX(last_execution_time) AS "Last Exec Time"
  ,SUM(CAST(execution_count AS numeric(38))) AS "Total Statement Exec Count"
  ,SUM(CAST(total_elapsed_time AS numeric(38))) / SUM(CAST(execution_count AS numeric(38))) / 1000.0 AS "Avg Exec Time[ms]"
  ,SUM(CAST(total_worker_time AS numeric(38))) / SUM(CAST(execution_count AS numeric(38))) / 1000.0 AS "Avg CPU Time[ms]"
  ,SUM(CAST(total_physical_reads AS numeric(38))) / SUM(CAST(execution_count AS numeric(38))) AS "Avg Physical Read Pages"
  ,SUM(CAST(total_logical_reads AS numeric(38))) / SUM(CAST(execution_count AS numeric(38))) AS "Avg Logical Read Pages"
  ,SUM(CAST(total_logical_writes AS numeric(38))) / SUM(CAST(execution_count AS numeric(38))) AS "Avg Logical Write Pages"
  ,SUM(CAST(total_clr_time AS numeric(38))) / SUM(CAST(execution_count AS numeric(38))) AS "Avg CRL Time[μs]"
  ,SUM(CAST(plan_generation_num AS numeric(38))) AS "Total Statement PlanGen Num(Recompile Num)"
  ,MAX(creation_time) AS "Last Statement PlanGen Time"
  ,SUM(CAST(size_in_bytes AS numeric(38)))/1024 AS "Total Statement Plan Size(KB)"
  ,SUM(CAST(total_rows AS numeric(38))) / SUM(CAST(execution_count AS numeric(38))) AS "Avg Rows" --SQL2012以降(2008もSP適用でサポート可)
  ,MAX(CAST(max_rows AS numeric(38))) AS "Max Rows" --SQL2012以降(2008もSP適用でサポート可)
  ,MIN(CAST(min_rows AS numeric(38))) AS "Min Rows" --SQL2012以降(2008もSP適用でサポート可)
  , MIN(text) AS "Text"
  , MIN(objtype) AS "Text Object Type"
  , MIN(cacheobjtype) AS "Text Object Cache Type"
  , MIN(plan_handle) AS "Text Plan Handle"
  ,SUM(CAST(usecounts AS numeric(38))) AS "Total Text Exec Count"
  ,CONVERT(xml, MIN(whole)) AS "Whole Query Plan"  -- 全体プラン出力
  ,CONVERT(xml, MIN(part)) AS "Part Query Plan"  -- 部分プラン出力
FROM
  ( SELECT
      total_elapsed_time, total_worker_time
      , total_physical_reads, total_logical_reads, total_logical_writes, total_clr_time
      , execution_count, plan_generation_num, creation_time, query_hash
      , total_rows, min_rows, max_rows --SQL2008以降
      , SUBSTRING(qt.text, (statement_start_offset/2) + 1,
        ((CASE statement_end_offset 
          WHEN -1 THEN DATALENGTH(qt.text)
          ELSE statement_end_offset END 
          - statement_start_offset)/2) + 1
        ) AS statement_text
      , last_execution_time
      , cp.plan_handle, cp.usecounts, cp.size_in_bytes, cp.objtype, cp.cacheobjtype
      , qt.text, qt.dbid
      , qp_whole.query_plan as whole  -- 全体プラン出力
      , qp_part.query_plan as part -- 部分プラン出力
    FROM sys.dm_exec_query_stats qs
      LEFT JOIN sys.dm_exec_cached_plans cp ON qs.plan_handle = cp.plan_handle
      CROSS APPLY sys.dm_exec_sql_text(sql_handle) qt
      CROSS APPLY sys.dm_exec_text_query_plan(cp.plan_handle, DEFAULT, DEFAULT) qp_whole  -- 全体プラン出力
      CROSS APPLY sys.dm_exec_text_query_plan(cp.plan_handle, statement_start_offset, statement_end_offset) qp_part  -- 部分プラン出力
    WHERE db_name(qt.dbid) not in ('msdb','master','tempdb') AND qt.dbid IS NOT NULL AND qt.dbid <> 32767 --Resource DBのdbidは常に 32767 固定 
--  WHERE db_name(qt.dbid) in ('msdb','master','tempdb') OR qt.dbid IS NULL OR qt.dbid = 32767 --Resource DBのdbidは常に 32767 固定
    /*
     -- CPUコストの高い Hash Match や Sort に絞る場合はここのコメントブロックを外す
    WHERE 
      query_plan LIKE '%Hash Match%' OR query_plan LIKE '%Sort%'
    */ 
--  WHERE q.plan_handle in (XXX for debug)
  ) AS dual
GROUP BY dual.query_hash
ORDER BY 8 DESC
OPTION(RECOMPILE)