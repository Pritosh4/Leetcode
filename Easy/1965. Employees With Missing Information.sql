SELECT employee_id
FROM Employees AS e 
LEFT JOIN Salaries AS s
USING(employee_id)
WHERE salary IS NULL 
UNION 
SELECT employee_id
FROM Salaries AS a
LEFT JOIN Employees AS e
USING(employee_id)
WHERE name IS NULL
ORDER BY employee_id;
