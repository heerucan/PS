t = int(input())

def rotation(graph,n):
    temp = []
    # 90도 회전
    for i in range(n):
        for j in range(n-1, -1, -1):
            temp.append(graph[j][i])

    new_graph = []
    for i in range(0,len(temp),n):
        new_graph.append(temp[i:i+n])
    return new_graph


for tc in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    first = rotation(graph,n)
    second = rotation(first,n)
    third = rotation(second,n)

    temp = [first, second, third]
    res = []
    for j in range(n):
        for i in temp:
            for k in range(n):
                res.append(i[j][k])

    print('#{}'.format(tc))
    for i in range(1,len(res)+1):
        print(res[i-1], end='')
        if i % n == 0:
            print(' ', end='')
        if i % (3*n) == 0:
            print()