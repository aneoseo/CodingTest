Table `Activities`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| sell_date   | date    |
| product     | varchar |
+-------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each row of this table contains the product name and the date it was sold in a market.
```

---

Write a solution to find for each date the number of different products sold and their names.

The sold products names for each date should be sorted lexicographically.

Return the result table ordered by `sell_date`.

---

Example

```
Input:
Activities table:
+------------+------------+
| sell_date  | product     |
+------------+------------+
| 2020-05-30 | Headphone  |
| 2020-06-01 | Pencil     |
| 2020-06-02 | Mask       |
| 2020-05-30 | Basketball |
| 2020-06-01 | Bible      |
| 2020-06-02 | Mask       |
| 2020-05-30 | T-Shirt    |
+------------+------------+
Output:
+------------+----------+------------------------------+
| sell_date  | num_sold | products                     |
+------------+----------+------------------------------+
| 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
| 2020-06-01 | 2        | Bible,Pencil                 |
| 2020-06-02 | 1        | Mask                         |
+------------+----------+------------------------------+
```

---

**Checkpoint**

- GROUP_CONCAT()
    - `GROUP BY`를 사용했을 때, 그룹별로 문자열들을 합치는 함수(집계 함수)
    - `CONCAT()`이 단일 행에서 여러 컬럼이나 문자열을 붙인다면, `GROUP_CONCAT()`은 여러 행의 값을 하나의 문자열로 합치고 싶을 때 사용
    - `SEPARATOR`를 이용해 연결 사이에 넣을 구분자 지정 가능