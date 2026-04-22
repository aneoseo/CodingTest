WITH RECURSIVE

-- 각 직원의 조직 레벨 구하기
hierarchy AS (
    SELECT
        employee_id,
        employee_name,
        manager_id,
        salary,
        1 AS level
    FROM Employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        e.salary,
        h.level + 1
    FROM Employees e
    JOIN hierarchy h
      ON e.manager_id = h.employee_id
),

-- 모든 관리자-부하 관계 펼치기
subordinates AS (
    SELECT
        manager_id,
        employee_id,
        salary
    FROM Employees
    WHERE manager_id IS NOT NULL

    UNION ALL

    SELECT
        s.manager_id,
        e.employee_id,
        e.salary
    FROM subordinates s
    JOIN Employees e
      ON e.manager_id = s.employee_id
)

-- 팀 규모와 예산 계산
SELECT
    h.employee_id,
    h.employee_name,
    h.level,
    COUNT(DISTINCT s.employee_id) AS team_size,
    h.salary + COALESCE(SUM(s.salary), 0) AS budget
FROM hierarchy h
LEFT JOIN subordinates s
  ON h.employee_id = s.manager_id
GROUP BY
    h.employee_id,
    h.employee_name,
    h.level,
    h.salary
ORDER BY
    h.level ASC,
    budget DESC,
    h.employee_name ASC;