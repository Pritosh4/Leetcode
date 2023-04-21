SELECT project_id, ROUND(AVG(experience_years), 2) AS average_years
FROM Project AS p
LEFT JOIN Employee AS e
USING(employee_id)
GROUP BY project_id;
