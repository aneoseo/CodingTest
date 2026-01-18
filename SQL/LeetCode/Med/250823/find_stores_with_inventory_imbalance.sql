WITH w1 AS (
    SELECT store_id, MAX(price) AS max_price, MIN(price) AS min_price
    FROM inventory
    GROUP BY store_id
    HAVING COUNT(DISTINCT product_name) >= 3
),
w2 AS (
    SELECT
        i.store_id,
        MAX(CASE WHEN i.price = w1.max_price THEN i.product_name END) AS most_exp_product,
        MAX(CASE WHEN i.price = w1.max_price THEN i.quantity END) AS most_exp_quantity,
        MAX(CASE WHEN i.price = w1.min_price THEN i.product_name END) AS cheapest_product,
        MAX(CASE WHEN i.price = w1.min_price THEN i.quantity END) AS cheapest_quantity
    FROM inventory i JOIN w1
        ON i.store_id = w1.store_id
    GROUP BY i.store_id
)
SELECT w2.store_id, s.store_name, s.location, w2.most_exp_product, w2.cheapest_product,
    ROUND(w2.cheapest_quantity/w2.most_exp_quantity, 2) AS imbalance_ratio
FROM w2 JOIN stores s
    ON w2.store_id = s.store_id
WHERE w2.most_exp_quantity < w2.cheapest_quantity
ORDER BY imbalance_ratio DESC, s.store_name;