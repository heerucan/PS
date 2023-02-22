# 테스트케이스 개수
# 체스판의 한 변의 길이 l (체스판의 크기는 l × l)

# 몇 번 움직이면 이동 가능하냐 -> 최단거리 -> BFS -> Queue

from collections import deque

# 나이트가 이동할 수 있는 칸
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(x, y, l):
    graph = [[0]*l for _ in range(l)]
    visited = [[False]*l for _ in range(l)]

    queue = deque()
    # 시작점을 추가하기
    queue.append((x, y))

    # 큐가 빌 때까지 돌아
    while queue:
        # 큐에 있는 요소를 빼
        x, y = queue.popleft()
    
        # 이동할 수 있는 칸을 for문을 돌면서
        for i in range(8):
            xx = x + dx[i]
            yy = y + dy[i]

            if xx >= 0 and xx < l and yy >= 0 and yy < l and not visited[xx][yy]:
                visited[xx][yy] = True
                graph[xx][yy] = graph[x][y] + 1
                queue.append((xx, yy))

    print(graph[A][B])
    return graph[A][B]

t = int(input())
while t != 0:
    l = int(input())
    # 나이트가 현재 있는 칸 - 출발점
    a, b = map(int, input().split())
    # 나이트가 이동하려고 하는 칸 - 도착점
    A, B = map(int, input().split())

    if a == A and b == B:
        print(0)
    else:
        bfs(a, b, l)

    t -= 1