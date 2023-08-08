-- 코드를 입력하세요
SELECT B.APNT_NO, A.PT_NAME, B.PT_NO, B.MCDP_CD, C.DR_NAME, B.APNT_YMD
FROM PATIENT A
JOIN APPOINTMENT B ON A.PT_NO = B.PT_NO
JOIN DOCTOR C ON B.MDDR_ID = C.DR_ID
WHERE B.APNT_YMD LIKE '2022-04-13%' AND B.MCDP_CD = 'CS' AND B.APNT_CNCL_YN = 'N'
ORDER BY APNT_YMD;