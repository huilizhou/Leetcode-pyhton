# Write your MySQL query statement below


select d.Name as Department,e1.Name as Employee, e1.Salary as Salary from Employee e1 inner join Department d on e1.DepartmentId=d.Id
where e1.Salary in (select Max(e2.Salary) from Employee e2 where e2.DepartmentId = e1.DepartmentId)