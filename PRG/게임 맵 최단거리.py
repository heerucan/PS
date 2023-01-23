from collections import deque
    
def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n = len(maps)
    m = len(maps[0])

    def bfs(x, y):
        queue = deque()
        queue.append((x,y))
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                
                if xx < 0 or xx >= n or yy < 0 or yy >= m:
                    continue

                if maps[xx][yy] == 0:
                    continue
                
                if maps[xx][yy] == 1:
                    maps[xx][yy] = maps[x][y] + 1
                    queue.append((xx, yy))

        if maps[n-1][m-1] == 1:
            return -1
        else:
            return maps[n-1][m-1]

    return bfs(0,0)

solution([[1,0,1,0,1],[1,0,1,0,1],[1,0,1,0,1],[1,1,1,0,1]]) # -1 
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]) # 11