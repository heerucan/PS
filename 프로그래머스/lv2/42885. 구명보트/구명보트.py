# 하나에 2명, 무게제한 있음
# 모든 사람 구하기 위해 필요한 구명보트 개수 최솟값?
# 스택을 사용하면 풀릴 것 같음, 근데 내가 간과한 게 순서대로 탈 필요가 없다는 것임.
# 무거운 순서대로 정렬 -> 무거운 거 스택에 넣고, 맨 뒤에서부터 작은 놈을 체크
from collections import deque
def solution(people, limit):
    cnt = 0
    people.sort(reverse=True)
    queue = deque(people)

    while queue:
        if queue[0] + queue[-1] > limit:
            queue.popleft()
            cnt += 1
        elif queue[0] + queue[-1] <= limit:
            queue.popleft()
            if len(queue) >= 1:
                queue.pop()
            cnt += 1
    
    return cnt
        