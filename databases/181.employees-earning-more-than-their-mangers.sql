# Write your MySQL query statement below

SELECT Worker.Name AS Employee FROM Employee AS Worker, Employee AS Manager WHERE Worker.ManagerId = Manager.Id AND Worker.Salary > Manager.Salary

select worker.name as Employee from Employee as worker,Employee as Manager where worker.ManagerId=Manager.Id and worker.Salary>Manager.Salary;