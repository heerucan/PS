import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u] += [v]
    graph[v] += [u]

visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)
