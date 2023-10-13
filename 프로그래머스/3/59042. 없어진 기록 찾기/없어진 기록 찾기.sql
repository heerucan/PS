-- 코드를 입력하세요
-- 입양 간 기록은 있고, 보호소에 들어온 기록이 없는 동물을 출력하기
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS I RIGHT OUTER JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL