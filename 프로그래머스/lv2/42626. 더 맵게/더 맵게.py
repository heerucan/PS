# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수
# 섞은 음식 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# k 이상으로 만들 수 없는 경우는 -1 반환
from heapq import heapify, heappushpop, heappop

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    # 모든 음식의 스코빌 지수의 가장 작은 값이 k보다 크거나 같은 경우 break
    while scoville[0] < K: 
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        heappushpop(scoville, heappop(scoville) + scoville[0]*2)
        answer += 1
        
    return answer