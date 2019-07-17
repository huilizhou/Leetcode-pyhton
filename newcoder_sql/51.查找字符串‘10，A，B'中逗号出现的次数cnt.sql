```
SELECT (length("10,A,B")-length(replace("10,A,B",",","")))/length(",") AS cnt
```