SELECT product_name, year, price
FROM Sales AS s
LEFT JOIN Product AS p
USING(product_id);
