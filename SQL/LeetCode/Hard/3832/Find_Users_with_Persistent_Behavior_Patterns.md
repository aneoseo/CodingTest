Table: `activity`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| user_id      | int     |
| action_date  | date    |
| action       | varchar |
+--------------+---------+
(user_id, action_date, action) is the primary key (unique value) for this table.
Each row represents a user performing a specific action on a given date.
```

---

Write a solution to identify behaviorally stable users based on the following definition:

- A user is considered behaviorally stable if there exists a sequence of at least `5`consecutive days such that:
    - The user performed exactly one action per day during that period.
    - The action is the same on all those consecutive days.
- If a user has multiple qualifying sequences, only consider the sequence with the maximum length.

Return *the result table ordered by* `streak_length` *in descending order*, *then by* `user_id` *in ascending order*.

---

Example

```
Input:
activity table:
+---------+-------------+--------+
| user_id | action_date | action |
+---------+-------------+--------+
| 1       | 2024-01-01  | login  |
| 1       | 2024-01-02  | login  |
| 1       | 2024-01-03  | login  |
| 1       | 2024-01-04  | login  |
| 1       | 2024-01-05  | login  |
| 1       | 2024-01-06  | logout |
| 2       | 2024-01-01  | click  |
| 2       | 2024-01-02  | click  |
| 2       | 2024-01-03  | click  |
| 2       | 2024-01-04  | click  |
| 3       | 2024-01-01  | view   |
| 3       | 2024-01-02  | view   |
| 3       | 2024-01-03  | view   |
| 3       | 2024-01-04  | view   |
| 3       | 2024-01-05  | view   |
| 3       | 2024-01-06  | view   |
| 3       | 2024-01-07  | view   |
+---------+-------------+--------+

Output:
+---------+--------+---------------+------------+------------+
| user_id | action | streak_length | start_date | end_date   |
+---------+--------+---------------+------------+------------+
| 3       | view   | 7             | 2024-01-01 | 2024-01-07 |
| 1       | login  | 5             | 2024-01-01 | 2024-01-05 |
+---------+--------+---------------+------------+------------+
```

---

**Checkpoint**

- `DATE_SUB(date, INTERVAL value unit)`
- `ROW_NUMBER() OVER (PARTITION BY ...)` : 같은 파티션 안에서 지정한 순서대로 번호를 붙임

- 유저의 특정 action이 연속적으로 이어졌는지 판단할 수 있는 컬럼 추가
    
    ```sql
    SELECT
        user_id,
        action,
        action_date,
        **DATE_SUB(
            action_date,
            INTERVAL ROW_NUMBER() OVER (
                PARTITION BY user_id, action
                ORDER BY action_date
            ) DAY
        ) AS consecutive_grp**
    FROM one_action_per_day
    ```
    
    1. `ROW_NUMBER() OVER (PARTITION BY ...)`
        | user_id | action | action_date | ROW_NUMBER() |
        | --- | --- | --- | --- |
        | 1 | login | 2024-01-01 | 1 |
        | 1 | login | 2024-01-02 | 2 |
        | 1 | login | 2024-01-03 | 3 |
        | 1 | login | 2024-01-04 | 4 |
        | 1 | login | 2024-01-05 | 5 |
        | 1 | logout | 2024-01-06 | 1 |
    2. `DATE_SUB(date, INTERVAL value unit)`
        | user_id | action | action_date | DATE_SUB() |
        | --- | --- | --- | --- |
        | 1 | login | 2024-01-01 | 2023-12-31 |
        | 1 | login | 2024-01-02 | 2023-12-31 |
        | 1 | login | 2024-01-03 | 2023-12-31 |
        | 1 | login | 2024-01-04 | 2023-12-31 |
        | 1 | login | 2024-01-05 | 2023-12-31 |
        | 1 | logout | 2024-01-06 | 2024-01-05 |