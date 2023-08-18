# 섬의 개수 세는 프로그램
# 정사각형과 가로/세로/대각선 연결된 사각형은 걸어갈 수 있는 사각형
# 지도의 너비 w, 높이 h
# 1은 땅, 0은 바다

# DFS

import sys
sys.setrecursionlimit(10**7)



def solution(w, h, graph):

    def dfs(x, y):
        #방문처리를 해줘야 함
        graph[x][y] = 0 # 방문처리를 0으로 해줘야 함

        # 상
        if x-1 >= 0 and x-1 < h:
            if graph[x-1][y] == 1:
                dfs(x-1, y)
        # 하
        if x+1 >= 0 and x+1 < h:
            if graph[x+1][y] == 1:
                dfs(x+1, y)
        # 좌
        if y-1 >= 0 and y-1 < w:
            if graph[x][y-1] == 1:
                dfs(x, y-1)
        # 우
        if y+1 >= 0 and y+1 < w:
            if graph[x][y+1] == 1:
                dfs(x, y+1)

        # 대각선
        if x-1 >= 0 and x-1 < h and y-1 >= 0 and y-1 < w:
            if graph[x-1][y-1] == 1:
                dfs(x-1, y-1)

        if x-1 >= 0 and x-1 < h and y+1 >= 0 and y+1 < w:
            if graph[x-1][y+1] == 1:
                dfs(x-1, y+1)

        if x+1 >= 0 and x+1 < h and y-1 >= 0 and y-1 < w:
            if graph[x+1][y-1] == 1:
                dfs(x+1, y-1)

        if x+1 >= 0 and x+1 < h and y+1 >= 0 and y+1 < w:
            if graph[x+1][y+1] == 1:
                dfs(x+1, y+1)
        
    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 0:
                continue
            else:
                dfs(i,j)
                result+=1
    
    print(result)
    return result

while True:
    w, h = map(int, input().split())
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    if w == 0 and h == 0:
        break
    else:
        solution(w, h, graph)
