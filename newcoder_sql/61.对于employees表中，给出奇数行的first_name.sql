```
SELECT E1.first_name FROM employees E1
WHERE (SELECT COUNT(*) FROM employees E2 WHERE E1.first_name>=E2.first_name)%2=1
```