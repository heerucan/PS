# 안전한 영역 -> 물에 잠기지 않은 그래프의 개수
# n이하 지점을 다 n으로 같게 만들어버려

# 안전영역 개수가 최대인 경우? -> 그 개수 출력
# dfs를 통해서 개수 체크해줘야 함

# 그러면 가장 작은수부터 개수 하나씩 체크

# 아무지역도 물에 잠기지 않을 수 있어!!!!!!!

import sys
sys.setrecursionlimit(10**7)

n = int(input())
visited = [[False]*n for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 높이를 담는 배열
height_array = []
for i in range(n):
    for j in range(n):
        if graph[i][j] not in height_array:
            height_array.append(graph[i][j])

height_array.sort()

def dfs(x,y,num):
    visited[x][y] = True

    for i in range(4):
        xx = dx[i]+x
        yy = dy[i]+y

        if xx < 0 or xx >= n or yy < 0 or yy >= n:
            continue

        if visited[xx][yy]:
            continue

        if 0<=xx<n and 0<=yy<n and not visited[xx][yy]:
            if graph[xx][yy] != num: # 안전영역을 찾는 것이니까 같으면 안됨
                dfs(xx,yy,num)


# height이하인 지점을 다 height로 바꾸는 함수
def change_height(height):
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= height:
                graph[i][j] = height


# height가 아닌 영역을 찾는 함수 = 안전영역의 개수 찾는 함수
def count_safety_place(height):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if graph[i][j] != height:
                    dfs(i,j,height)
                    cnt += 1
    return cnt

# 안전영역 최대 개수를 담는 변수
res = 0
for i in height_array:
    change_height(i)
    cnt = count_safety_place(i)
    if cnt >= res:
        res = cnt
    if res == 0: # 아무곳도 안 잠길 수 있대..
        res = 1
    visited = [[False]*n for _ in range(n)]

print(res)