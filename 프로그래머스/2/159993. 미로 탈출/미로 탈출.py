#bfs
from collections import deque

def solution(maps):
    answer = 0 
    n,m = len(maps), len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dx,dy = [-1,1,0,0], [0,0,-1,1]
    temp = []
    
    def bfs(xy,endX,endY):
        visited = [[0 for _ in range(m)] for _ in range(n)]
        queue = deque()
        queue.append(xy)
        
        while queue:
            x,y = queue.popleft()

            for i in range(4):
                xx = dx[i]+x
                yy = dy[i]+y

                if 0 > xx or xx > n-1 or 0 > yy or yy > m-1 or maps[xx][yy] == 'X':
                    continue

                if visited[xx][yy] == 0:
                    queue.append((xx,yy))
                    visited[xx][yy] = visited[x][y]+1
                
        return visited[endX][endY]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                temp.append((i,j))
                
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'L':
                temp.append((i,j))
                
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'E':
                temp.append((i,j))
    
    start = bfs(temp[0],temp[1][0],temp[1][1])
    end = bfs(temp[1],temp[2][0],temp[2][1])
    
    if start == 0 or end == 0:
        return -1
    else:
        return start+end
        