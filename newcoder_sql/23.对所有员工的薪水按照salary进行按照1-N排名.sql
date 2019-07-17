```
对所有员工的当前(to_date='9999-01-01')薪水按照salary进行按照1-N的排名，相同salary并列且按照emp_no升序排列
CREATE TABLE `salaries` (
`emp_no` int(11) NOT NULL,
`salary` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`from_date`));
```
```
SELECT s1.emp_no,s1.salary,COUNT(DISTINCT s2.salary)
FROM salaries s1,salaries s2
WHERE s1.to_date='9999-01-01' AND s2.to_date='9999-01-01'
AND s1.salary<=s2.salary
GROUP BY s1.emp_no
ORDER BY s1.salary DESC,s1.emp_no
```