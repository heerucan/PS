-- 코드를 입력하세요
# 난관 : 해당 시간대에 없어도 그냥 0으로 카운트해줘야 함 -> Recursive문으로 해결가능

# Recursive문으로 임시테이블 생성
WITH RECURSIVE TEMP_TABLE (HOUR) AS ( # 재귀쿼리 세팅
    SELECT 0 # 초기값 설정
    UNION ALL  # 위 쿼리와 아래 쿼리의 값을 합하는 연산
    SELECT HOUR + 1 
    FROM TEMP_TABLE # 하나씩 불려 나감 
    WHERE HOUR < 23 # 반복을 멈추는 용도
)


# LEFT OUTER JOIN : 왼쪽 테이블 기준으로, 왼쪽은 다 가져오고 - 오른쪽 테이블에서 왼쪽에 속한 값이 없어도 다 가져와
# 즉, 예를 들어, ANIMAL_OUTS의 데이트 타임에 2시가 없어도 그냥 가져옴
SELECT A.HOUR, COUNT(HOUR(B.DATETIME)) AS COUNT
FROM TEMP_TABLE A
LEFT OUTER JOIN ANIMAL_OUTS B
ON A.HOUR = HOUR(B.DATETIME)
GROUP BY HOUR
ORDER BY HOUR