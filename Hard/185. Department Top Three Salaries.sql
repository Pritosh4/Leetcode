SELECT D.name AS Department, E1.name as Employee, E1.salary AS Salary
FROM Employee AS E1
JOIN Department AS D
ON E1.departmentId = D.id
WHERE 3 > (SELECT COUNT(DISTINCT E2.salary)
           FROM Employee AS E2
           WHERE E2.salary > E1.salary AND E2.departmentId = E1.departmentId);
