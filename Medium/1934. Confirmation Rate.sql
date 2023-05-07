SELECT user_id, ROUND(IFNULL(SUM(CASE WHEN action = 'confirmed' THEN 1 END)/COUNT(action),0), 2) AS confirmation_rate
FROM Signups AS s
LEFT JOIN Confirmations AS c
USING (user_id)
GROUP BY user_id
