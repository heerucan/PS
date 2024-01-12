-- 그러면, 먼저, 내림차순 정렬이 필요
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FAVORITES, FOOD_TYPE) IN (

    SELECT MAX(FAVORITES), FOOD_TYPE
    FROM REST_INFO
    GROUP BY FOOD_TYPE
)
ORDER BY FOOD_TYPE DESC;
