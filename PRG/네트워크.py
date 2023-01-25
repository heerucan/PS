# 컴퓨터의 개수 n
# 연결에 대한 정보 2차원 배열 computers
# 연결요소 - 네트워크의 개수(결국 노드덩어리임) -> DFS스택 재귀함수
import sys
sys.setrecursionlimit(10**7)

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False]*n
    
    # graph = [[1번 컴에 연결된 n번 컴터], ... ]
    # 여기에는 각 그래프 1번 컴퓨터에 연결된 컴퓨터들을 추가하는 것
    for i in range(0, n):
        for j in range(0, n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)
                
    # 그래프를 돌 dfs도 만들었음
    def dfs(x):
        visited[x] = True

        for i in graph[x]:
            if not visited[i]:
                dfs(i)

    # 컴터 개수만큼 dfs를 도는데 이때 연결된 네트워크 counting (처음 도는 dfs를 여기서 counting)
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
    # print(answer)
    return answer


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])