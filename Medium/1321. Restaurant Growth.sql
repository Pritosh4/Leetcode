SELECT c.visited_on, SUM(cu.amount) AS amount, ROUND(SUM(cu.amount) / 7, 2) AS average_amount
FROM (SELECT DISTINCT visited_on FROM Customer) AS c
INNER JOIN Customer AS cu
ON DATEDIFF(c.visited_on, cu.visited_on) BETWEEN 0 AND 6
GROUP BY c.visited_on
HAVING COUNT(DISTINCT cu.visited_on) > 6;
