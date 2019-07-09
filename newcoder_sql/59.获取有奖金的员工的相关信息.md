```
SELECT e.emp_no, e.first_name, e.last_name, b.btype, s.salary, 
(CASE b.btype 
 WHEN 1 THEN s.salary * 0.1
 WHEN 2 THEN s.salary * 0.2
 ELSE s.salary * 0.3 END) AS bonus
FROM employees AS e INNER JOIN emp_bonus AS b ON e.emp_no = b.emp_no
INNER JOIN salaries AS s ON e.emp_no = s.emp_no AND s.to_date = '9999-01-01'
```