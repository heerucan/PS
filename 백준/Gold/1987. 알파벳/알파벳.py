# 세로R, 가로C
# 좌측 상단에서 시작 0,0
# 상하좌우 이동 가능
# 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

# bfs, 경로 개수 체크라고 생각했는데 dfs였음
# 생각해보니, 한 노드로 쭉 가다가 겹치는 알파벳있으면 다른 노드로 틀어야 하기 때문임
# 어차피 dfs는 모든 노드를 다 탐색하니까 최대칸을 찾을 수 있긴 함

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 지나온 알파벳을 set자료형을 이용해 방문표시하고 dfs로 탐색
# 첫 시작점 알파벳 추가
visited = set(graph[0][0])

answer = 0

def dfs(x,y,cnt):
    global answer
    answer = max(answer, cnt)

    #상하좌우 순서대로 탐색
    for i in range(4):
        xx = dx[i] + x
        yy = dy[i] + y

        if 0 > xx or xx >= r or 0 > yy or yy >= c:
            continue

        if 0 <= xx < r and 0 <= yy < c:
            if graph[xx][yy] not in visited:
                visited.add(graph[xx][yy])
                dfs(xx,yy,cnt+1)
                visited.remove(graph[xx][yy])
                
dfs(0,0,1)
print(answer)
