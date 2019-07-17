```
SELECT "select count(*) from " || name || ";" AS cnts
FROM sqlite_master WHERE type = 'table'
```