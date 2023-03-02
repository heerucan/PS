# 촌수 계산하는 프로그램
# 전체 사람 수 n
# 둘째 줄 : 촌수 계산해야 하는 서로 다른 두 사람 번호
# 셋째 줄 : 부모 자식 간의 관계의 개수 m
# 넷째 줄 : 부모 자식 간의 관계를 나타내는 두 번호 x, y (x-부모, y-자식)
# 촌수 계산할 필요없으면 -1 반환

# DFS

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]

total = -1
def dfs(x, depth):
    # 현재 노드를 방문처리부터 한다.
    # 현재 노드와 인접한 노드들을 재귀적으로 방문한다.
    visited[x] = True
    global total

    # a랑 b가 같은 노드 연결 요소에 속해서 b가 x랑 같으면 결국 연결되어 있는 것임
    if x == b:
        total = depth # total에 depth를 할당해주면 되는 것임
        return total

    for i in graph[x]:
        if not visited[i]:
            dfs(i, depth+1)

dfs(a,0)
print(total)