# 부서별로 신청한 금액이 들어있는 배열 d
# 예산 budget
# 최대 몇 개의 부서에 지원할 수 있는지 반환

# 가장 신청 금액이 적은 부서부터 지원

def solution(d, budget):
    answer = 0
    
    # d 배열을 오름차순 정렬
    # d를 돌면서 budget에서 하나씩 빼다가 budget이 0보다 작아지는 순간 stop
    d.sort()
    
    for i in d:
        budget -= i
        if budget >= 0:
            answer += 1
        else:
            break
    
    return answer