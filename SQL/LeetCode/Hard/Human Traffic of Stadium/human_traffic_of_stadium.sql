WITH FilteredStadium AS (
    SELECT *
    FROM stadium
    WHERE people >= 100
), GroupedStadium AS (
    SELECT *,
        id - ROW_NUMBER() OVER(ORDER BY id) AS grp  -- id와 행 번호의 차이가 같으면 연속된 숫자
    FROM FilteredStadium
)

SELECT id, visit_date, people
FROM GroupedStadium
WHERE grp IN (SELECT grp
	        FROM GroupedStadium
	        GROUP BY grp
	        HAVING COUNT(*) >= 3)
ORDER BY visit_date;