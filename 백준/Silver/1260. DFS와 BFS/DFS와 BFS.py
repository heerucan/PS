import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split(' '))
# 인접리스트 : graph의 인덱스가 각 노드 번호를 말하는 것이고, 해당 노드 별로 연결된 노드를 담는 것 : 메모리효율굿, 속도느림
# 인접행렬 : 노드 i->j로 가는 간선이 있으면 1을 없으면 0을 넣는 것 : 메모리 낭비O, 속도 빠름

# 여기서는 인접리스트를 사용하였고, 앞으로 인접리스트를 사용할 것임
graph = [[] for _ in range(n+1)] # 노드개수 + 1(0포함)
visited = [False]*(n+1) # 노드개수 + 1(0포함)

# 간선의 개수만큼 for문을 돌려야 함 - 노드 간 연결 관계 자체가 간선을 의미
for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
# dfs - 재귀
def dfs(graph, x, visited):
    visited[x] = True
    print(x, end=' ')
    graph[x].sort()
    for i in graph[x]:
        if not visited[i]:
            dfs(graph, i, visited)


# bfs - 큐
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = False
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if visited[i]:
                queue.append(i)
                visited[i] = False

dfs(graph, v, visited)
print()
bfs(graph, v, visited)