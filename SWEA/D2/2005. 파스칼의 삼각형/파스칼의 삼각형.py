t = int(input())

# DP 문제!
for tc in range(1, t+1):
    n = int(input())
    graph = [[] for _ in range(n)]

    print('#{}'.format(tc))
    for i in range(n):
        for j in range(i+1): 
            if i == 0 or j == 0 or j == i: #가장자리는 1
                graph[i].append(1)
                print(1, end=' ')
            else: #점화식!
                graph[i].append(graph[i-1][j-1]+graph[i-1][j])
                print(graph[i-1][j-1]+graph[i-1][j], end=' ')
        print()