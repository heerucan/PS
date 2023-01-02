import sys
# 1부터 n까지 자연수 중 중복 없이 m개 고른 수열

# 재귀함수 사용
# 개수가 m개가 아니면, n까지의 숫자 확인 후 
# 방문했는지 체크해서 방문X 숫자를 기준으로 재귀함수 호출

N, M = map(int, input().split())
visited = [0] * N # N만큼의 방문처리 공간을 위한 배열 만듦
arr = []

def backtracking(cnt):
    if cnt == M: # 어느 순간 cnt가 m과 같아지면 return
        print(*arr)
        return

    for i in range(N):
        if visited[i] == 0: # 방문하지 않았다면
            visited[i] = 1  # 방문처리를 해주고
            arr.append(i+1) # 1부터 더해(왜냐면, i는 0부터 시작임)
            backtracking(cnt+1)  # 다음 깊이 탐색 -> 재귀함수 호출
            visited[i] = 0  # 탐사 완료 후 다시 초기화
            arr.pop()  # 배열에 추가한 값도 다시 제거

backtracking(0)