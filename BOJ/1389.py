# 케빈 베이컨의 수가 가장 적은 사람을 구하기 
# (오름차순으로 한 명만 출력)
# n : 유저의 수
# m : 친구 관계의 수

# 플로이드 워셜 방법으로 먼저 풀기

n, m = map(int, input().split())

INF = int(1e9)
# n+1인 이유는 1번~5번이지만 배열인덱스는 0부터 시작이라
graph = [[INF]*(n+1) for _ in range(n+1)] 

for _ in range(m): # 친구관계 대입하기
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 자기자신은 0을 대입
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 1->3은 거리가 1로 바로 갈 수 있지만,
# 1->2는 1->k->2처럼 누군가를 거쳐서 가기 때문에 이렇게 해줘야 한다.
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 가장 작은 케빈 베이컨의 합을 가진 수를 찾기
arr = []
for i in range(0, n+1):
    arr.append(sum(graph[i]))
    
print(arr.index(min(arr)))