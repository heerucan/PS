from collections import deque

def solution(x, y, n):
    answer = -1
    graph = [0]*1000001
    visited = [0]*1000001
    queue = deque()
    
    queue.append(x)
    
    while queue:
        x = queue.popleft()
        
        if x == y:
            answer = graph[x]
            break
        
        for xx in (x+n, x*2, x*3):
            if xx >= 0 and xx <= 1000000 and not visited[xx]:
                visited[xx] = 1
                graph[xx] = graph[x] + 1
                queue.append(xx)
    return answer

solution(10, 40, 5)
solution(10, 40, 30)
solution(2, 5, 4)