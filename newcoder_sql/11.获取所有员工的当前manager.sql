```
获取所有员工当前的manager，如果当前的manager是自己的话结果不显示，当前表示to_date='9999-01-01'。
结果第一列给出当前员工的emp_no,第二列给出其manager对应的manager_no。
CREATE TABLE `dept_emp` (
`emp_no` int(11) NOT NULL,
`dept_no` char(4) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`dept_no`));
CREATE TABLE `dept_manager` (
`dept_no` char(4) NOT NULL,
`emp_no` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`dept_no`));
```

```
SELECT dept_emp.emp_no,dept_manager.emp_no as manager_no
FROM dept_emp,dept_manager
WHERE dept_emp.emp_no<>dept_manager.emp_no
AND dept_emp.dept_no=dept_manager.dept_no
AND dept_emp.to_date='9999-01-01'
AND dept_manager.to_date='9999-01-01'
```