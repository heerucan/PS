# dfs
import sys
sys.setrecursionlimit(10**7)

def solution(maps):
    answer = []
    dx,dy = [-1,1,0,0], [0,0,-1,1]
    n,m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    def dfs(x,y,res):
        visited[x][y] = True   
        res = int(maps[x][y])       
        
        for i in range(4):
            xx = dx[i]+x
            yy = dy[i]+y
            
            if 0>xx or xx>n-1 or 0>yy or yy>m-1 or maps[xx][yy]=='X':
                continue
                
            if not visited[xx][yy]:
                res += dfs(xx,yy,res)

        return res
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(dfs(i,j,0))
                
    if not answer:
        return [-1]
    else:
        return sorted(answer)