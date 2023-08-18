import sys
sys.setrecursionlimit(10**7)

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input()))

def dfs(x, y):
    # myColor는 현재 내 좌표의 대문자를 의미
    myColor = graph[x][y]
    # 내 현재 위치 방문처리를 해주고 (소문자로 바꿔서 방문처리)
    graph[x][y] = graph[x][y].lower() # 소문자화 라이브러리
        # if graph[x][y] == 'R':
        #     graph[x][y] = 'r'
    
        # if graph[x][y] == 'G':
        #     graph[x][y] = 'g'

        # if graph[x][y] == 'B':
        #     graph[x][y] = 'b'

    # 내 다음 좌표가 나랑 색이 같은지 체크해서 같으면 dfs돌기
    if x-1 >= 0 and x-1 < n:
        if graph[x-1][y] == myColor:
            dfs(x-1, y)

    if x+1 >= 0 and x+1 < n:
        if graph[x+1][y] == myColor:
            dfs(x+1, y)

    if y-1 >= 0 and y-1 < n:
        if graph[x][y-1] == myColor:
            dfs(x, y-1)

    if y+1 >= 0 and y+1 < n:
        if graph[x][y+1] == myColor:
            dfs(x, y+1)

normal = 0
jaejun = 0

# 적록색약 아닌 사람 체크하기
for i in range(n):
    for j in range(n):
        # 이미 방문처리된 아이들은 냅두고
        if graph[i][j] == 'r' or graph[i][j] == 'g' or graph[i][j] == 'b':
            continue
        # 처음 방문하는 아이들만 counting -> 그게 첫 dfs 아이들이니까!
        else:
            dfs(i,j)
            normal += 1

# 아닌 사람 체크 후 소문자로 바뀐 graph -> 대문자화 + R -> G로 변경
for i in range(n):
    for j in range(n):
        graph[i][j] = graph[i][j].upper()
        if graph[i][j] == 'R':
            graph[i][j] = 'G'


# 적록색약 체크하기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'g' or graph[i][j] == 'b':
            continue
        else:
            dfs(i,j)
            jaejun += 1

print(normal, jaejun)
