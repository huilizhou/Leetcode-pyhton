```
查找所有员工自入职以来的薪水涨幅情况，给出员工编号emp_no以及其对应的薪水涨幅growth，并按照growth进行升序
CREATE TABLE `employees` (
`emp_no` int(11) NOT NULL,
`birth_date` date NOT NULL,
`first_name` varchar(14) NOT NULL,
`last_name` varchar(16) NOT NULL,
`gender` char(1) NOT NULL,
`hire_date` date NOT NULL,
PRIMARY KEY (`emp_no`));
CREATE TABLE `salaries` (
`emp_no` int(11) NOT NULL,
`salary` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`from_date`));
```


```
SELECT sCurrent.emp_no, (sCurrent.salary-sStart.salary) AS growth
FROM (SELECT s.emp_no, s.salary FROM employees e LEFT JOIN salaries s ON e.emp_no = s.emp_no WHERE s.to_date = '9999-01-01') AS sCurrent
INNER JOIN (SELECT s.emp_no, s.salary FROM employees e LEFT JOIN salaries s ON e.emp_no = s.emp_no WHERE s.from_date = e.hire_date) AS sStart
ON sCurrent.emp_no = sStart.emp_no
ORDER BY growth
```