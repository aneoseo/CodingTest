WITH ranked AS (
    SELECT employee_id, rating, 
    ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY review_date DESC) AS rn
    FROM performance_reviews
), last3 AS (
    SELECT employee_id,
        MAX(CASE WHEN rn = 1 THEN rating END) AS r1,
        MAX(CASE WHEN rn = 2 THEN rating END) AS r2,
        MAX(CASE WHEN rn = 3 THEN rating END) AS r3
    FROM ranked
    WHERE rn <= 3
    GROUP BY employee_id
)

SELECT e.employee_id, e.name, (l.r1 - l.r3) AS improvement_score
FROM last3 l JOIN employees e
    ON e.employee_id = l.employee_id
WHERE l.r3 IS NOT NULL
    AND l.r3 < l.r2
    AND l.r2 < l.r1
ORDER BY improvement_score DESC, e.name ASC;