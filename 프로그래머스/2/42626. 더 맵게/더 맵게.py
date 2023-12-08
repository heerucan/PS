# 가장낮은 거 + (두번째로 낮은거*2)
import heapq
def solution(scoville, k):
    answer,new = 0,0
    scoville.sort()
    
    while scoville[0] < k:
        if len(scoville) >= 2:
            new = heapq.heappop(scoville)+heapq.heappop(scoville)*2
            heapq.heappush(scoville, new)
            answer += 1    
        else:
            answer = -1
            break
    
    return answer