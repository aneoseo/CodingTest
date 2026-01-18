-- 오답 코드

-- WITH C1 AS (
--     SELECT customer_id
--     FROM customer_transactions
--     WHERE transaction_type = 'purchase'
--     GROUP BY customer_id
--     HAVING COUNT(transaction_type) >= 3
-- ), C2 AS (
--     SELECT customer_id
--     FROM customer_transactions
--     GROUP BY customer_id
--     HAVING DATEDIFF(MAX(transaction_date),MIN(transaction_date))+1 >= 30
-- ), C AS (
--     SELECT customer_id, IFNULL(COUNT(transaction_type),0) refund
--     FROM customer_transactions
--     WHERE transaction_type = 'refund'
--     GROUP BY customer_id
-- ), C3 AS (
--     SELECT C.customer_id
--     FROM customer_transactions t
--         JOIN C ON t.customer_id = C.customer_id
--     GROUP BY customer_id
--     HAVING refund/COUNT(transaction_type) <= 0.2
-- )

-- SELECT customer_id
-- FROM C1
--     JOIN C2 ON C1.customer_id = C2.customer_id
--     JOIN C3 ON C1.customer_id = C3.customer_id
-- ORDER BY 1


-- 정답 코드

WITH transactions_summary AS (
    SELECT customer_id,
        SUM(transaction_type = 'purchase') AS purchase_count,
        SUM(transaction_type = 'refund') AS refund_count,
        COUNT(*) AS total_count,
        DATEDIFF(MAX(transaction_date), MIN(transaction_date)) + 1 AS active_days
    FROM customer_transactions
    GROUP BY customer_id
)
SELECT customer_id
FROM transactions_summary
WHERE purchase_count >= 3
  AND active_days >= 30
  AND (refund_count / total_count) < 0.2
ORDER BY customer_id;