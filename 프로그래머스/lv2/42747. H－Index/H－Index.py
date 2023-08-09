def solution(citations):
    answer = []
    citations.sort()
    
    
    for h in range(len(citations)+1):
        big = 0
        small = 0
        for j in citations:
            if j >= h: #기준값보다 인용횟수가 큰 경우
                big += 1
            else:
                small += 1
        
        if big >= h and small <= h:
            answer.append(h)
    
    return answer[-1]