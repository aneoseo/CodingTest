WITH weekly_meetings AS (
    SELECT employee_id,
        DATE_ADD(meeting_date, INTERVAL -WEEKDAY(meeting_date) DAY) AS week_start,
        SUM(duration_hours) AS total_hours
    FROM meetings
    GROUP BY employee_id, week_start
), heavy_meetings AS (
    SELECT employee_id, week_start
    FROM weekly_meetings
    WHERE total_hours > 20
)
SELECT e.employee_id, employee_name, department, COUNT(*) AS meeting_heavy_weeks
FROM heavy_meetings m
    JOIN employees e ON m.employee_id = e.employee_id
GROUP BY e.employee_id, employee_name, department
HAVING COUNT(*) >= 2
ORDER BY 4 DESC, 2 ASC;