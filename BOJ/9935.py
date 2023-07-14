import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int, input().split()))

stack = [] # (인덱스)를 저장하고, 항상 현재탑과 비교하기 위해 이전탑을 저장
result = [0]*n

# 현재 자기자신보다 더 큰 놈의 (인덱스+1)를 찾는 것
for i in range(n-1, -1, -1): # 4-> 3-> 2-> 1-> 0
    # 즉, 현재탑보다 그 다음 탑이 더 높을 경우, stack[-1][0] -> 인덱스
    while stack and tops[stack[-1]] < tops[i]:
        result[stack[-1]] = i+1 #result 각 인덱스에 수신탑의 번호 대입
        # stack(즉, 이전탑을 저장한 곳) 
        # pop해주는 이유는 : 현재탑과 이전탑을 비교했고 -> 이전탑보다 현재탑이 더 커서 -> 신호 받을 놈을 찾았기에 pop
        stack.pop()
        
    stack.append(i)

print(*result)