# 1번 컴터를 통해 바이러스에 걸리게 되는 컴퓨터의 수를 출력하기

c = int(input()) # 컴퓨터의 수
v = int(input()) #  네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

graph = [[] for i in range(c+1)]
for _ in range(v):
    a, b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

visited = [False]*(c+1)
totalVirus = 0

def dfs(x):
    global totalVirus
    virus = 0
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            virus += 1
    totalVirus += virus    

dfs(1) # 1번 컴퓨터부터 체크 시작

print(totalVirus)