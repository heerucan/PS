import sys
input = sys.stdin.readline
from collections import deque

# 최단경로 구하는 문제
# 벽 부술 수 있는 개수가 최대 1개,

n,m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
# 3차원 행렬을 통해 - 벽 부순 것을 체크
# visited[x][y][0] 벽 부술 수 있음 / visited[x][y][1] 벽 부술 수 없음
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(startX,startY,cnt):
    queue = deque()
    # 큐에 시작 위치 삽입
    queue.append((startX,startY,cnt)) # x좌표, y좌표, 부순횟수
    visited[startX][startY][cnt] = 1

    while queue:
        x,y,break_cnt = queue.popleft()

        if (x,y) == (n-1, m-1):
            return visited[x][y][break_cnt]
        
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y            

            if 0 > xx or xx >= n or 0 > yy or yy >= m:
                continue
            
            if 0 <= xx <= n-1 and 0 <= yy <= m-1:
                # 벽인 경우 즉, 1인 경우 + 벽을 깬 적이 없을 경우 -> 벽을 부수고 이동
                if graph[xx][yy] == 1 and break_cnt == 0:
                    visited[xx][yy][1] = visited[x][y][0] + 1
                    queue.append((xx, yy, 1))

                # 벽이 아닌 경우 즉, 0인 경우 + 한 번도 방문한 적 없을 경우 -> 벽을 안부수고 이동
                elif graph[xx][yy] == 0 and visited[xx][yy][break_cnt] == 0:
                    visited[xx][yy][break_cnt] = visited[x][y][break_cnt] + 1
                    queue.append((xx,yy,break_cnt))
    return -1

print(bfs(0,0,0))