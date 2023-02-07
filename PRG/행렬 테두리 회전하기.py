# 상변 : x,y -> x, y+1
# 하변 : x,y -> x, y-1
# 좌변 : x,y -> x-1, y
# 우변 : x,y -> x+1, y
# (x-1)*columns + y
# queries에 있는 것대로 회전 다하고 각 회전마다 최솟값 반환

# 1. 먼저 그래프 만들어서 행렬을 그리기
# 2. 테두리 이동하는 거 구해주기
# [[1,2,3,4,5,6], [7,8,9,10,11,12], ...]

def solution(rows, columns, queries):
    answer = []
    # 행렬 그래프 만들기
    graph = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
    num = 1
    for row in range(1, rows+1):
        for column in range(1, columns+1):
            graph[row][column] = num
            num += 1
    
    # [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
    for x1, y1, x2, y2 in queries:
        tmp = graph[x1][y1]
        minValue = tmp # 가장 최소값은 가장 왼쪽 상단 꼭짓점좌표니까 여기에 저장
        
        # 좌변 x,y -> x-1, y
        # 14 : 3,2 -> 2,2
        # y값은 y1으로 같음
        for k in range(x1+1, x2+1): #8빼고 3~5 시작해서 +1을 더함
            change = graph[k][y1] # value에 좌표값을 저장
            graph[k-1][y1] = change # 해당 좌표에 value값을 저장
            minValue = min(minValue, change)

        # 하변 x,y -> x, y-1
        # 27 : 5,3 -> 5,2
        # x값은 x2로 같음
        for k in range(y1+1, y2+1): #26빼고 27~28 +1 더함
            change = graph[x2][k]
            graph[x2][k-1] = change
            minValue = min(minValue, change)

        # 우변 x,y -> x+1, y
        # 10 : 2,4 -> 3,4
        # y값은 y2로 같음
        for k in range(x2-1, x1-1, -1):
            change = graph[k][y2]
            graph[k+1][y2] = change
            minValue = min(minValue, change)

        # 상변 x,y -> x, y+1
        # 8 : 2,2 -> 2,3
        # x값은 x1으로 같음
        for k in range(y2-1, y1-1, -1):
            change = graph[x1][k]
            graph[x1][k+1] = change
            minValue = min(minValue, change)
        
        # 처음 8을 tmp에 저장했고, 그 후에 그럼 8은 (2,2) -> (2,3)으로 이동했다.
        # 그래서 이동을 시켜준 걸 새롭게 그래프좌표에 저장해준다.
        graph[x1][y1+1] = tmp
        # queries 돌 때마다 가장 작은 값을 answer 배열에 추가
        answer.append(minValue)
    # print(answer)
    return answer

solution(6,6,[[2,2,5,4]])
# solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])