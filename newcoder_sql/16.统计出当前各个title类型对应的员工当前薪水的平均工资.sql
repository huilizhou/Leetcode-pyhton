```
CREATE TABLE `salaries` (
`emp_no` int(11) NOT NULL,
`salary` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`from_date`));
CREATE TABLE IF NOT EXISTS "titles" (
`emp_no` int(11) NOT NULL,
`title` varchar(50) NOT NULL,
`from_date` date NOT NULL,
`to_date` date DEFAULT NULL);

```

```
SELECT t.title,AVG(s.salary) as avg
FROM titles t
INNER JOIN salaries s
ON t.emp_no=s.emp_no
WHERE s.to_date='9999-01-01'
AND t.to_date='9999-01-01'
GROUP BY t.title
```