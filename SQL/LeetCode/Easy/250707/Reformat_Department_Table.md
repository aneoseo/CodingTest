Table: `Department`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| revenue     | int     |
| month       | varchar |
+-------------+---------+
In SQL,(id, month) is the primary key of this table.
The table has information about the revenue of each department per month.
The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].
```

---

Reformat the table such that there is a department id column and a revenue column for each month.

Return the result table in any order.

---

Example

```
Input:
Department table:
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+
Output:
+------+-------------+-------------+-------------+-----+-------------+
| id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1    | 8000        | 7000        | 6000        | ... | null        |
| 2    | 9000        | null        | null        | ... | null        |
| 3    | null        | 10000       | null        | ... | null        |
+------+-------------+-------------+-------------+-----+-------------+
```

---

"""Checkpoint"""

- 테이블에서 하나의 칼럼에 있는 행 값들을 펼쳐 각각을 하나의 칼럼으로 만들어 주는 것
    - `PIVOT` : 데이터를 행기반에서 열기반으로 바꾸는 것
    - `UNPIVOT` : PIVOT된 것을 다시 열기반에서 행기반으로 바꾸는 것
- MySQL에서는 `PIVOT` 구문을 직접 지원하지 않음
    - 세로로 길게 늘어진(=롱폼 데이터) `month`를 가로로 펼치고, 각 `id`의 `month`별 `revenue`를 합산해 담아야 함
    - `CASE WHEN`으로 조건을 걸어 해당 `month`에만 값을 노출
    - `SUM`으로 집계하여 각 `id`의 월별 `revenue` 총합을 계산
    - 결과적으로 `id`별 월별 매출을 피봇테이블처럼 와이드하게 변환