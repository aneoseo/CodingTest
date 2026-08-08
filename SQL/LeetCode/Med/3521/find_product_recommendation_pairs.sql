SELECT pp1.product_id AS product1_id, pp2.product_id AS product2_id, 
        p1.category AS product1_category, p2.category AS product2_category, 
        COUNT(DISTINCT pp1.user_id) AS customer_count 
FROM ProductPurchases pp1
    LEFT JOIN ProductPurchases pp2
        ON pp1.user_id = pp2.user_id AND pp1.product_id < pp2.product_id 
    JOIN ProductInfo p1
        ON pp1.product_id = p1.product_id 
    JOIN ProductInfo p2
        ON pp2.product_id = p2.product_id
GROUP BY pp1.product_id, pp2.product_id, p1.category, p2.category 
HAVING COUNT(DISTINCT pp1.user_id) >= 3
ORDER BY 5 DESC, product1_id,  product2_id