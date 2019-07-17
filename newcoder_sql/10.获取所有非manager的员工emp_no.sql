```
获取所有非manager的员工emp_no
CREATE TABLE `dept_manager` (
`dept_no` char(4) NOT NULL,
`emp_no` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`dept_no`));
CREATE TABLE `employees` (
`emp_no` int(11) NOT NULL,
`birth_date` date NOT NULL,
`first_name` varchar(14) NOT NULL,
`last_name` varchar(16) NOT NULL,
`gender` char(1) NOT NULL,
`hire_date` date NOT NULL,
PRIMARY KEY (`emp_no`));
```

```
SELECT e.emp_no 
FROM employees e
LEFT JOIN dept_manager d
ON e.emp_no=d.emp_no
WHERE d.dept_no is NULL
```

```
SELECT e.emp_no 
FROM employees e
WHERE e.emp_no NOT IN (SELECT d.emp_no FROM dept_manager d)
```