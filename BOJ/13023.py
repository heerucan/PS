# 그래프의 깊이가 5인 것을 찾아내라!!!
# 있으면 1, 없으면 0

import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

# 그래프를 그려!
graph = [[] for _ in range(n)]

# 인접리스트임
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리 체크용 배열
visited = [False]*n

result = False

def dfs(x, depth):
    global result

    if depth == 5: # 만약 깊이가 5면 1을 출력
        result = True
        exit()

    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth+1)
            # 여기서 방문처리를 다시 false로 하는 이유는,
            # dfs를 빠져나온 다는 것은 -> 제일 깊은 곳까지 찍고 나온 것
            # 근데도 깊이가 5가 되지 않았다면 다른 방식으로 깊이 탐색을 하게끔 방문처리를 해제 해주는 것.
            visited[i] = False

for i in range(n):
    if not visited[i]:
        visited[i] = True
        dfs(i,1)
        visited[i] = False
        if result: # 이걸 안해주면 시간초과남
            break

if result:
    print(1)
else:
    print(0)

