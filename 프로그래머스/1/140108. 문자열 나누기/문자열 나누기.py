def solution(s):
    answer = 0
    xCnt, yCnt = 0, 0
    
    for i in s:
        if xCnt == yCnt:
            answer += 1
            k = i
        if i == k:
            xCnt += 1
        else:
            yCnt += 1
            
    return answer