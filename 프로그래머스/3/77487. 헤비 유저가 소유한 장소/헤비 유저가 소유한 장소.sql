-- 코드를 입력하세요
-- 공간을 둘 이상 등록한 사람을 "헤비 유저"
SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(HOST_ID) >= 2
)
ORDER BY ID;