SELECT s.score, (SELECT COUNT(DISTINCT(d.score)) 
                  FROM Scores AS d
                  WHERE d.score >= s.score) AS 'rank'
FROM Scores AS s
ORDER BY s.score DESC;
