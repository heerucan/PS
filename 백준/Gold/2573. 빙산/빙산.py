import sys
sys.setrecursionlimit(10**4)
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,-1,1] 

def melt(graph):
    array = deque([])
    for i in range(1,n-1):
        for j in range(1,m-1):
            if graph[i][j] !=0:
                check_list = [graph[i-1][j],graph[i+1][j],graph[i][j-1],graph[i][j+1]]
                array.append(check_list.count(0))

    for i in range(1,n-1):
        for j in range(1,m-1):
            if graph[i][j] != 0:
                arround = array.popleft()
                graph[i][j] -= arround
                if graph[i][j] < 0:
                    graph[i][j] = 0    
    return graph

def dfs(graph, visited, x,y):
    visited[x][y] = True

    for i in range(4):
        xx = dx[i]+x
        yy = dy[i]+y

        if 0<=xx<n and 0<=yy<m and not visited[xx][yy]:
            if graph[xx][yy] != 0:
                dfs(graph,visited,xx,yy)

year = 0
while True:
    cnt = 0
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] != 0:
                dfs(graph, visited, i,j)
                cnt += 1

    if cnt > 1:
        print(year)
        break
    else:
        year += 1
        graph = melt(graph)
        if sum(map(sum,graph)) == 0:
            print(0)
            break