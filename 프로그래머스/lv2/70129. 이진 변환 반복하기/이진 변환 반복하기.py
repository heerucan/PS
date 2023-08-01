# 1. 0제거
# 2-1. 0이 제거된 x의 길이 = c
# 2-2. c에 맞는 이진수를 가져오기

# 위 과정을 반복하면서 -> 최종적으로 1로 만들기
# [제거된 0개수, 몇 번이나 단계를 반복했는지 그 횟수]
# bin() -> 십진수 -> 이진수
def solution(s):
    answer = []
    
    zeroCnt = 0
    cnt = 0
    
    while s != '1':
        zeroCnt += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        cnt += 1
        
        if s == '1':
            return [cnt, zeroCnt]
            break
