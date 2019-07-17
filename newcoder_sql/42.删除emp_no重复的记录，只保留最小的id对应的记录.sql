```
DELETE FROM titles_test WHERE id NOT IN 
(SELECT MIN(id) FROM titles_test GROUP BY emp_no)
```