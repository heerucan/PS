from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    sort_queue = deque(sorted(queue, reverse=True))
    
    idx = deque()
    for i in range(len(queue)):
        idx.append(i)
    
    cnt = 0
    while queue:
        a = queue.popleft()
            
        if a != sort_queue[0]:
            queue.append(a)
            idx.append(idx.popleft())
        else:
            cnt += 1
            sort_queue.popleft()
            idx_value = idx.popleft()
            if idx_value == location:
                answer = cnt
                break
                
    return answer