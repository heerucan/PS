def solution(n):
    cnt = 0
    for i in range(1, n+1): # 1~15
        answer = 0
        for j in range(i, n+1):
            answer += j
            # print(i, j, answer)
            if answer == n:
                cnt += 1
                break
            if answer > n:
                break
            
    return cnt