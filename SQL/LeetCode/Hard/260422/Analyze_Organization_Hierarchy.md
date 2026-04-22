Table: `Employees`

```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| employee_id    | int     |
| employee_name  | varchar |
| manager_id     | int     |
| salary         | int     |
| department     | varchar |
+----------------+----------+
employee_id is the unique key for this table.
Each row contains information about an employee, including their ID, name, their manager's ID, salary, and department.
manager_id is null for the top-level manager (CEO).
```

---

Write a solution to analyze the organizational hierarchy and answer the following:

1. Hierarchy Levels: For each employee, determine their level in the organization (CEO is level 1, employees reporting directly to the CEO are level 2, and so on).
2. Team Size: For each employee who is a manager, count the total number of employees under them (direct and indirect reports).
3. Salary Budget: For each manager, calculate the total salary budget they control (sum of salaries of all employees under them, including indirect reports, plus their own salary).

Return the result table ordered by the result ordered by `level` in ascending order, then by `budget` in descending order, and finally by `employee_name` in ascending order.

---

Example:

```
Input:
Employees table:
+-------------+---------------+------------+--------+-------------+
| employee_id | employee_name | manager_id | salary | department  |
+-------------+---------------+------------+--------+-------------+
| 1           | Alice         | null       | 12000  | Executive   |
| 2           | Bob           | 1          | 10000  | Sales       |
| 3           | Charlie       | 1          | 10000  | Engineering |
| 4           | David         | 2          | 7500   | Sales       |
| 5           | Eva           | 2          | 7500   | Sales       |
| 6           | Frank         | 3          | 9000   | Engineering |
| 7           | Grace         | 3          | 8500   | Engineering |
| 8           | Hank          | 4          | 6000   | Sales       |
| 9           | Ivy           | 6          | 7000   | Engineering |
| 10          | Judy          | 6          | 7000   | Engineering |
+-------------+---------------+------------+--------+-------------+

Output:
+-------------+---------------+-------+-----------+--------+
| employee_id | employee_name | level | team_size | budget |
+-------------+---------------+-------+-----------+--------+
| 1           | Alice         | 1     | 9         | 84500  |
| 3           | Charlie       | 2     | 4         | 41500  |
| 2           | Bob           | 2     | 3         | 31000  |
| 6           | Frank         | 3     | 2         | 23000  |
| 4           | David         | 3     | 1         | 13500  |
| 7           | Grace         | 3     | 0         | 8500   |
| 5           | Eva           | 3     | 0         | 7500   |
| 9           | Ivy           | 4     | 0         | 7000   |
| 10          | Judy          | 4     | 0         | 7000   |
| 8           | Hank          | 4     | 0         | 6000   |
+-------------+---------------+-------+-----------+--------+
```

---

**Checkpoint**

- 재귀 CTE
    
    ```sql
    WITH RECURSIVE  -- CTE 중 하나만 재귀여도 RECURSIVE는 전체에 붙음
    
    	cte1 AS (  -- 재귀 CTE 조건
    		SELECT ...              -- anchor (시작)
    		UNION ALL
    		SELECT ... FROM 자기자신  -- recursive step
    	),
    	
    	cte2 AS (...)  -- 재귀가 아니어도 상관 없음
    ```