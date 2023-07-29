import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, len(graph)):
    print(len(graph[i]))