# BFS 최단경로를 요구하는 문제니까!
# 1: 이동가능, 0: 이동불가능

from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

#상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # 시작 위치 큐에 삽입

    while queue:
        x, y = queue.popleft()
        
        # 해당 칸의 상하좌우 다 체크 (인접한 노드들 체크)
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if xx < 0 or xx >= n or yy < 0 or yy >= m: 
                continue
            
            if graph[xx][yy] == 1: # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                graph[xx][yy] = graph[x][y] + 1
                queue.append((xx, yy))
    return graph[n-1][m-1] # n, m이 n-1, m-1임

print(bfs(0, 0))