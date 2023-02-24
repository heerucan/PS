# 숨바꼭질, bfs, 실버1
# 1. 그래프를 어떻게 그려줘야 할 것인지 고민
# 2. 방문처리 관련해서 고민했음

# bfs -> 최단거리 구하는 것임 -> queue

from collections import deque

# n 수빈이 위치
# k 동생 위치
n, k = map(int, input().split())

# 범위가 (0 ≤ N, K ≤ 100,000)
graph = [0]*100001
visited = [0]*100001

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = 1

    while queue:
        x = queue.popleft()

        # 1초 후에 수빈이가 이동 가능한 구역 
        # x-1, x+1, 2*x 방향을 위한 배열
        dx = [-1, 1, x]
        for i in range(3):
            xx = x + dx[i]
            if xx >= 0 and xx <= 100000 and visited[xx] == 0:
                visited[xx] = 1
                graph[xx] = graph[x] + 1
                queue.append(xx)
        
    print(graph[k])
    return graph[k]

bfs(n)
