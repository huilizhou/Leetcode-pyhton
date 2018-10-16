# Write your MySQL query statement below
SELECT Name as Customers FROM Customers WHERE ID not in (SELECT C.id FROM Customers as C, Orders as O where C.Id=O.CustomerID);
