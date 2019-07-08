```
SELECT dept_no,group_concat(emp_no) AS employees
FROM dept_emp
GROUP BY dept_no
```