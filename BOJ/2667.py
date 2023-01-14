# 1은 집있는 곳, 0은 없는 곳
# 출력값 : 총단지수, 단지내의 집의 수를 오름차순으로 정렬

import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    else:
        if graph[x][y] == 1:
            global count
            count += 1
            graph[x][y] = 0
            # 상하좌우 체크 인접한 노드 체크
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
    return False

result = 0
count = 0
arr = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            arr.append(count)
            result += 1
            count = 0

print(result)
arr.sort()
for i in arr:
    print(i)

