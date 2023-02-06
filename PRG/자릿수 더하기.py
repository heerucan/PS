def solution(n):
    answer = 0
    stringListN = list(str(n))
    
    for i in stringListN:
        answer += int(i)
    return answer