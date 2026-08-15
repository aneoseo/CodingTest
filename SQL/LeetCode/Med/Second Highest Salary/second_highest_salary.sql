-- 오답 코드

-- WITH Ranking AS (
--     SELECT *, DENSE_RANK() OVER (ORDER BY salary DESC) AS salaryRank
--     FROM Employee
-- )

-- SELECT salary AS SecondHighestSalary
-- FROM Ranking
-- WHERE salaryRank = 2;

-- 만약 결과가 null 값이라면 화면에 아무것도 출력되지 않음


-- 오답 코드

-- WITH Ranking AS (
--     SELECT *, DENSE_RANK() OVER (ORDER BY salary DESC) AS salaryRank
--     FROM Employee
-- )

-- SELECT IFNULL(salary, 'null') AS SecondHighestSalary
-- FROM Ranking
-- WHERE salaryRank = 2;


-- 정답 코드

WITH Ranking AS (
    SELECT *, DENSE_RANK() OVER (ORDER BY salary DESC) AS salaryRank
    FROM Employee
)

SELECT MAX(CASE WHEN salaryRank = 2 THEN salary ELSE NULL END) AS SecondHighestSalary
FROM Ranking;