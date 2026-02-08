-- 하루에 한 가지 action만 하는 유저 조회
WITH one_action_per_day AS (
    SELECT
        user_id,
        action_date,
        MAX(action) AS action
    FROM activity
    GROUP BY user_id, action_date
    HAVING COUNT(*) = 1
),
-- 유저의 특정 action이 연속적으로 이어졌는지 판단할 수 있는 컬럼 추가
consecutive_check AS (
    SELECT
        user_id,
        action,
        action_date,
        DATE_SUB(
            action_date,
            INTERVAL ROW_NUMBER() OVER (
                PARTITION BY user_id, action
                ORDER BY action_date
            ) DAY
        ) AS consecutive_grp
    FROM one_action_per_day
),
-- 유저의 특정 action이 연속적으로 이어진 기간 컬럼 추가
streak AS (
    SELECT
        user_id,
        action,
        COUNT(*) AS streak_length,
        MIN(action_date) AS start_date,
        MAX(action_date) AS end_date
    FROM consecutive_check
    GROUP BY user_id, action, consecutive_grp
),
-- 유저별로 최장 연속 기간 순으로 번호 부여
best_per_user AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY streak_length DESC, start_date ASC, action ASC
        ) AS rn
    FROM streak
)

-- 5일 이상 연속으로 동일한 action을 한 stable 유저 조회
-- 한 유저가 여러 stable 케이스를 지닌다면, 최장 기간만 조회
SELECT
    user_id,
    action,
    streak_length,
    start_date,
    end_date
FROM best_per_user
WHERE rn = 1 AND streak_length >= 5
ORDER BY streak_length DESC, user_id ASC;