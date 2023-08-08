# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수
# 섞은 음식 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# k 이상으로 만들 수 없는 경우는 -1 반환
import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    
    # 이게 문제인 것 같음 일단 -> O(N) 굳이 넣어줄 필요가 있나?
    for i in scoville:
        heapq.heappush(heap, i)
    
    while heap[0] < K: # 모든 음식의 스코빌 지수의 가장 작은 값이 k보다 크거나 같은 경우 break
        if len(heap) == 1 and heap[0] < K:
            return -1
        
        mixed_scoville = heapq.heappop(heap) + heapq.heappop(heap) * 2
        heapq.heappush(heap, mixed_scoville)
        answer += 1
        
    return answer