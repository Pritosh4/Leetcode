SELECT name, SUM(amount) AS balance
FROM Users AS u
LEFT JOIN Transactions AS t
USING(account)
GROUP BY account
HAVING SUM(amount) > 10000;
