Table: `Accounts`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.
```

---

Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

- `"Low Salary"`: All the salaries strictly less than `$20000`.
- `"Average Salary"`: All the salaries in the inclusive range `[$20000, $50000]`.
- `"High Salary"`: All the salaries strictly greater than `$50000`.

The result table must contain all three categories. If there are no accounts in a category, return `0`.

Return the result table in any order.

---

Example

```
Input:
Accounts table:
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+
Output:
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+
```

---

**Checkpoint**

- `GROUP BY`는 존재하는 값만 반환하기 때문에 `IFNULL(COUNT(...), 0)`은 해당 그룹 자체가 없으면 아무 효과 없음