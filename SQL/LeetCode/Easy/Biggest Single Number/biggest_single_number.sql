-- 오답 코드

-- WITH maxcount AS (
--     SELECT MAX(num) maxnum, COUNT(num) countnum
--     FROM MyNumbers
--     GROUP BY num
-- )

-- SELECT 
--     CASE
--         WHEN countnum >= 2 THEN 'null'
--         ELSE maxnum
--     END num
-- FROM maxcount


-- 정답 코드

SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS singles;