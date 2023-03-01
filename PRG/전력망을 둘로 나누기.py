# n개의 송전탑이 전선을 통해 하나의 트리 형태
# 2개로 분할

#    1
#    |
#    3
#   / \
#  2   4
#     /|\
#    5 6 7
#       / \
#      8   9

# 송전탑의 개수 n
# wires는 전선으로 연결된 두 노드의 리스트

# dfs 모든 노드를 다 탐색해야 하기에 적합할 것 같음

import sys
sys.setrecursionlimit(10**7)
        
def solution(n, wires):
    answer = -1
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    
    # 인접리스트로 만듦 (무방향그래프)
    for i in wires:
        a = i[0]
        b = i[1]
        graph[a].append(b)
        graph[b].append(a)
   
    # [[], [3], [3], [1, 2, 4], [3, 5, 6, 7], [4], [4], [4, 8, 9], [7], [7]]

    # wires에서 전선이 끊어진 모든 경우의 수를 돌면서 최솟값을 찾아야 함.
    # 예를 들어, wires = [[1,2], [2,3], [3,4]]면 각각을 제거한 경우 총 3가지를 기록해야 한다.

    # x노드를 시작으로 방문된 노드의 개수 반환
    def dfs(x, visited, graph):
        visited[x] = True
        count = 1 # 방문한 노드의 개수
        for i in graph[x]:
            if not visited[i]:
                count += dfs(i, visited, graph)
        return count

    for i in range(len(wires)):
        a, b = wires[i]
        visited = [False]*(n+1)

        # 예를 들어, a = 1, b = 3 일 때, 
        # graph[1]에 연결된 3을 제거하고, graph[3]에 연결된 1을 제거
        graph[a].remove(b)
        graph[b].remove(a)

        # a번 노드로 시작 노드를 지정해 dfs를 돌고, 방문된 노드 개수를 count에 저장
        countA = dfs(a, visited, graph)
        countB = n - countA
        if answer != -1:
            # 연결된 노드의 개수 (즉, 방문한 노드의 개수 = count)이면
            answer = min(answer, abs(countA-countB))
        else:
            answer = abs(countA-countB)
        # 계산 후에는 다시 원상복구를 위해 추가
        graph[a].append(b)
        graph[b].append(a)
  
    return answer

# solution(4,[[1,2],[2,3],[3,4]])
solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
# solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])