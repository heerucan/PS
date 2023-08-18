# dfs로 그래프 개수 세기
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(graph, visited, x, y):
    # 대각선까지 추가
    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]

    visited[x][y] = True
    
    for i in range(8):
        xx = dx[i] + x
        yy = dy[i] + y

        if 0 > xx or xx > h-1 or 0 > yy or yy > w-1:
            continue

        if 0 <= xx <= h-1 and 0 <= yy <= w-1:
            if not visited[xx][yy] and graph[xx][yy] == 1:
                dfs(graph, visited, xx, yy)
                visited[xx][yy] = True

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    visited = [[False for _ in range(w)] for _ in range(h)]
    cnt = 0

    for _ in range(h):
        graph.append(list(map(int, input().rstrip().split())))

    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                if graph[i][j] == 1:
                    dfs(graph, visited, i,j)
                    cnt += 1
    print(cnt)