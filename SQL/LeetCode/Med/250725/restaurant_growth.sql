SELECT c2.visited_on,
    SUM(c1.amount) AS amount,
    ROUND(SUM(c1.amount) / 7, 2) AS average_amount
FROM Customer c1 JOIN Customer c2
    ON c1.visited_on BETWEEN DATE_SUB(c2.visited_on, INTERVAL 6 DAY) AND c2.visited_on
GROUP BY c2.visited_on
HAVING COUNT(DISTINCT c1.visited_on) = 7
ORDER BY c2.visited_on;