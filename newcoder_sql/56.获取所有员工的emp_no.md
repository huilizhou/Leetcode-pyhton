```
SELECT de.emp_no, de.dept_no, eb.btype, eb.recevied
FROM dept_emp AS de LEFT JOIN emp_bonus AS eb 
ON de.emp_no = eb.emp_no
```