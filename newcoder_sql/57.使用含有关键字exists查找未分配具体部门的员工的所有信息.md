```
SELECT * FROM employees WHERE NOT EXISTS 
(SELECT emp_no FROM dept_emp WHERE emp_no = employees.emp_no)
```