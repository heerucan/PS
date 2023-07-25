import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[-1]*m for _ in range(n)]

# 최단거리 - bfs
# 0은 갈 수 없어 -> 0 그대로 출력
# 1은 갈 수 있어 -> 여기 중 도달할 수 없으면 -1, 갈 수 있으면 거리
# 2는 목표지점

dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 0

    while queue:    
        x,y = queue.popleft()

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < n and 0 <= yy < m and visited[xx][yy] == -1:
                if graph[xx][yy] == 1:
                    visited[xx][yy] = visited[x][y] + 1
                    queue.append((xx,yy))
                elif graph[xx][yy] == 0:
                    visited[xx][yy] = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and visited[i][j] == -1:
            bfs(i,j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()