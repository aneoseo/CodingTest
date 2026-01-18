-- 오답 코드

-- WITH Category AS (
--     SELECT account_id, income, 
--         CASE
--             WHEN income < 20000 THEN 'Low Salary'
--             WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
--             WHEN income > 50000 THEN 'High Salary'
--         END AS category
--     FROM Accounts
-- )

-- SELECT category, IFNULL(COUNT(category), 0) accounts_count
-- FROM Category
-- GROUP BY 1


-- 정답 코드

WITH Salary AS (
    SELECT account_id, income, 
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
            WHEN income > 50000 THEN 'High Salary'
        END AS category
    FROM Accounts
), Categories AS (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
)

SELECT C.category, IFNULL(COUNT(S.category), 0) accounts_count
FROM Categories C LEFT JOIN Salary S
    ON C.category = S.category
GROUP BY S.category