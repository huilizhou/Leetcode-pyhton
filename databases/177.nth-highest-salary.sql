CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  declare m int;
SET m
= N - 1;
RETURN (
      #
Write your MySQL query statement below.
SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT m, 1 
  );
END