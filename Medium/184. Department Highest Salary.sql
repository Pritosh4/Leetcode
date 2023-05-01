SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee AS e
LEFT JOIN Department as d
ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) in (SELECT departmentId, MAX(SALARY)
                  FROM Employee
                  GROUP BY departmentId)
