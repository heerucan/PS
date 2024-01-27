# 적 : 파란 B
# 나 : 흰색 W

import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split(" "));

graph = []
visited = [[False]*n for _ in range(m)]
for i in range(m):
    graph.append(list(input()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,color):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    cnt = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y

            if 0 > xx or xx >= m or 0 > yy or yy >= n:
                continue

            if visited[xx][yy]:
                continue

            if 0 <= xx < m and 0 <= yy < n and not visited[xx][yy]:
                if graph[xx][yy] == color:
                    visited[xx][yy] = True
                    queue.append((xx,yy))
                    cnt += 1
    return cnt

white, blue = 0,0
for i in range(m):
    for j in range(n):
        if graph[i][j] == "W" and not visited[i][j]:
            white += bfs(i,j,"W")**2
        elif graph[i][j] == "B" and not visited[i][j]:
            blue += bfs(i,j,"B")**2

print(white, blue)