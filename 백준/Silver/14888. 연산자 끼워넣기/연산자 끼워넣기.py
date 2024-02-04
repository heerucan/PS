n = int(input())
a_array = list(map(int, input().split()))
cal_array = list(map(int, input().split()))

# 연산자들의 조합이잖아? 근데 순서가 필요해 -> 그러면 연산자 순열인 거 아녀?
visited = [False * n]

# a 배열의 숫자와 주어진 연산자를 통해서 만들 수 있는 결과의 최대/최소 출력

# 백트래킹으로 하겠지. 근데 졸라 백트래킹 모르겠어요;;;;;
# 그래프의 깊이

# temp = a_array[0]
max_val = float('-inf')
min_val = float('inf')

def backtracking(start, temp):
    global max_val, min_val
    
    # 그래프의 레벨이 a_array 길이와 같을 때 반환
    if start == n:
        max_val = max(max_val, temp)
        min_val = min(min_val, temp)
        return

    for i in range(len(cal_array)):
        if cal_array[i] > 0:            
            cal_array[i] -= 1 # 연산자 사용 표시
            # 연산자에 맞게 계산처리
            total = 0
            if i == 0:
                total = temp + a_array[start]
            elif i == 1:
                total = temp - a_array[start]
            elif i == 2:
                total = temp * a_array[start]
            elif i == 3:
                if temp > 0:
                    total = temp // a_array[start]
                else: # 음수를 양수로 나눌 때 
                    total = -(-temp // a_array[start])
            backtracking(start+1, total)
            cal_array[i] += 1 # 백트래킹 후 사용한 연산자 반환

backtracking(1, a_array[0])

print(max_val)
print(min_val)