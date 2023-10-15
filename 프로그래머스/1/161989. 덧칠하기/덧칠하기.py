from collections import deque
def solution(n, m, section):
    queue = deque(section)
    answer = 1
    a = queue[0]+m-1
    
    while queue:
        if a >= queue[0]:
            queue.popleft()
        else:
            answer += 1
            a = queue[0]+m-1
            
    return answer