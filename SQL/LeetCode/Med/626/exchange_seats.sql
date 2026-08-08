SELECT id, 
    CASE
        WHEN id = (SELECT COUNT(*) FROM Seat) AND id % 2 = 1 THEN student
        WHEN id % 2 = 1 THEN LEAD(student, 1) OVER (ORDER BY id)
        WHEN id % 2 = 0 THEN LAG(student, 1) OVER (ORDER BY id)
    END AS student
FROM Seat