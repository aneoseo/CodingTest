Table: `Seat`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
The ID sequence always starts from 1 and increments continuously.
```

---

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by `id` in ascending order.

---

Example

```
Input:
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+
Output:
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+
```

---

**Checkpoint**

- 윈도우 함수 (Window Function)
    - 행과 행 간의 관계를 정의하기 위해서 제공되는 함수
    - 순위, 합계, 평균, 행 위치 등을 조작
    ```
    SELECT WINDOW_FUNCTION(ARGUMENTS) OVER (PARTITION BY 칼럼
    										ORDER BY WINDOWING절)
    FROM 테이블명;
    ```
    - 행 순서 관련 WINDOW_FUNCTION
        - `LAG(칼럼, n)` : 파티션에서 n만큼 앞선 데이터를 반환
            - n의 기본값 1 = 이전 행
            - 결과가 NULL일 경우 표기되는 Default 값을 세 번쨰 인자값으로 지정 가능
        - `LEAD(칼럼, n)` : 파티션에서 n만큼 뒤에 있는 데이터를 반환
            - n의 기본값 1 = 다음 행
            - 결과가 NULL일 경우 표기되는 Default 값을 세 번쨰 인자값으로 지정 가능