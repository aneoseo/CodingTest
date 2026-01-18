SELECT E.employee_id
FROM Employees E LEFT JOIN Salaries S
    ON E.employee_id = S.employee_id
WHERE name IS NULL OR salary IS NULL

UNION

SELECT S.employee_id
FROM Employees E RIGHT JOIN Salaries S
    ON E.employee_id = S.employee_id
WHERE name IS NULL OR salary IS NULL

ORDER BY 1;