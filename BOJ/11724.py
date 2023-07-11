# 연결요소의 개수
# : 나누어진 각각의 그래프를 의미 

# dfs로 풀 수 있어.
# 깊이를 탐색하다가 그 다음 노드와 연결됐는지 체크해야 하니까

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split(' '))
# 그래프랑 방문체크 배열 만들기
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split(' '))
    graph[u].append(v)
    graph[v].append(u)

# [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

def dfs(x, depth):
    visited[x] = True

    for i in graph[x]:
        if not visited[i]:
            dfs(i, depth+1)

count = 0
for i in range(1, n+1):
    # 1 -> 2, 5 True (+1)
    # 2 -> 이미 1에서 True라 패스
    # 3 -> 4, 6 True (+1)
    # 4 -> 이미 3에서 True라 패스
    # 5 -> 이미 1에서 True라 패스
    # 6 -> 이미 3에서 True라 패스
    if visited[i] == False:
        dfs(i, 0)
        count += 1

print(count)