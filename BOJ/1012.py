# 0은 배추X, 1은 배추O
# 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로
# 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사
# 결국 연결요소 구하는 문제니까 dfs로 풀자! : dfs는 스택을 사용하는 것

# m : 배추밭의 가로
# n : 세로
# k : 배추 개수



import sys
sys.setrecursionlimit(10**7)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    else:
        # 1인 아이들에 한해서 탐색시 방문처리로 0으로 바꾸고, 상하좌우 탐색
        # 연결요소 개수 카운팅! 필요! 
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
    return False

# 테스트케이스 입력받아서 돌기
for _ in range(int(input())):
    graph = []
    m, n, k = map(int, input().split())

    graph = [[0]*m for _ in range(n)]

    # 좌표 받아서 1로 바꾸기
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    worm = 0
    for i in range(0, n):
        for j in range(0, m):
            if dfs(i, j) == True:
                worm += 1

    print(worm)