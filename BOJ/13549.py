# 숨바꼭질3, bfs, 골드5
# 기존 숨바꼭질 문제에서 바뀐 것 -> 순간이동이 0초 걸림

# bfs -> 최단거리 구하는 것임 -> queue

from collections import deque

# n 수빈이 위치
# k 동생 위치
n, k = map(int, input().split())

# 범위가 (0 ≤ N, K ≤ 100,000)
graph = [0]*100001
visited = [0]*100001

def bfs(x, visited, graph):
    queue = deque()
    queue.append([x])
    
    while queue:
        x = queue.popleft()

        if x == k: # k, 동생이 있는 곳과 같은 경우 반환
            print(graph[x])
            return graph[x]
        
        # 1초 후에 수빈이가 이동 가능한 구역 
        # x-1, x+1, 2*x 방향을 위한 배열
        dx = [-1, 1, x]
        for i in dx:
            if i != x:
                xx = x + i
            else:
                xx = x*2

            if xx >= 0 and xx <= 100000 and visited[xx] == 0:
                visited[xx] = 1
                graph[xx] = graph[x] + 1
                queue.append(xx)
        
bfs(n, visited, graph)