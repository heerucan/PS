-- 코드를 입력하세요
-- 2022.10.16에 대여중인 차 - 대여중 // 대여X - 대여 가능
SELECT CAR_ID, MAX(
    CASE WHEN '2022-10-16' < DATE_FORMAT(START_DATE, '%Y-%m-%d') THEN '대여 가능' 
    WHEN '2022-10-16' > DATE_FORMAT(END_DATE, '%Y-%m-%d') THEN '대여 가능' 
    ELSE '대여중' END
) AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;