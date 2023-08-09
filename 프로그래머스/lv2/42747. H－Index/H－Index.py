def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for h in range(len(citations)+1):
        big = 0
        for j in citations:
            if j >= h: #기준값보다 인용횟수가 큰 경우, 즉-> h번 이상 인용된 논문의 개수
                big += 1
        if big >= h:
            answer = h
    return answer