import heapq

def solution(k, score):
    answer = []
    score_h = []

    while score:
        score_value = score.pop(0)
        # 길이가 k보다 크면 -> 마지막 추가값이 min값보다 크면 -> h에 넣고 + 기존 가장 작은 값 삭제 + 그후 작은 값 출력
        if len(score_h) >= k and min(score_h) <= score_value:
            heapq.heappush(score_h,score_value)
            heapq.heappop(score_h)
            answer.append(score_h[0])
        elif len(score_h) >= k and min(score_h) > score_value:
            answer.append(score_h[0])
        elif len(score_h) < k:
            heapq.heappush(score_h,score_value)
            answer.append(score_h[0])
        
    return answer