# 상하좌우에 영향
# 며칠이 지나면 토마토가 다 익는지 최소일수 다 구하기
# m : 가로
# n : 세로
# 1 익은토마토, 0 익지 않은토마토, -1 토마토없는 칸

# BFS 큐
from collections import deque

# 그래프를 그리기
m, n = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

# 방문체크용 배열도 그려
visited = [[False]*m for _ in range(n)]

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
tomato = 0

queue = deque()

for i in range(n):
    for j in range(m):
        # 그래프에 0이 없으면(안익은 토마토가 없으면) -> 0 출력
        if 0 not in graph[i]:
            answer = 1 # 원래는 0을 출력하면 되는데 날짜개념상 첫 하루도 1일로 카운트되어서 1을 쳐줌
        else: # 토마토 전체 개수를 구해~
            if graph[i][j] == 0 or graph[i][j] == 1:
                tomato += 1
            if graph[i][j] == 1: # 좌표값이 1인 아이들의 x, y를 큐에 미리 넣어두기
                queue.append((i, j))


while queue:
    x, y = queue.popleft()
    visited[x][y] = True

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if xx >= 0 and xx < n and yy >= 0 and yy < m:
            if not visited[xx][yy] and graph[xx][yy] == 0:
                visited[xx][yy] = True
                graph[xx][yy] = graph[x][y] + 1
                queue.append((xx, yy))
                answer = graph[xx][yy]

# 모든 그래프 좌표 다 방문을 하면 False -> True로 방문처리가 될 것임
# 그러면 그 뜻은 True인 것은 익은 토마토들이고, True 개수와 방문 전 1,0인 토마토 개수가 일치하는지 체크해줘야 함
# 일치하면 다 방문했고, == 토마토가 다 익은 것임 // 일치하지 않으면 토마토가 익지 않은 게 있다는 뜻
trueCount = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == True:
            trueCount += 1

if trueCount != tomato:
    print(-1)
else:
    print(answer-1) # 첫 날이 포함되니까 1을 빼줌