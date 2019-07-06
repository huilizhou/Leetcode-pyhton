```
汇总各个部门当前员工的title类型的分配数目，结果给出部门编号dept_no、dept_name、其当前员工所有的title以及该类型title对应的数目count
CREATE TABLE `departments` (
`dept_no` char(4) NOT NULL,
`dept_name` varchar(40) NOT NULL,
PRIMARY KEY (`dept_no`));
CREATE TABLE `dept_emp` (
`emp_no` int(11) NOT NULL,
`dept_no` char(4) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`dept_no`));
CREATE TABLE IF NOT EXISTS `titles` (
`emp_no` int(11) NOT NULL,
`title` varchar(50) NOT NULL,
`from_date` date NOT NULL,
`to_date` date DEFAULT NULL);

```

```
SELECT de.dept_no,de.dept_name,t.title,count(t.title) as count
FROM (titles t JOIN dept_emp d ON t.emp_no=d.emp_no AND d.to_date='9999-01-01' AND t.to_date='9999-01-01')
JOIN departments de ON d.dept_no=de.dept_no
GROUP BY de.dept_no,de.dept_name,t.title 
ORDER BY de.dept_no,de.dept_name,t.title 
```