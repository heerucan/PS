def solution(n):
    answer = 0
    prime = [True]*(n+1)
    m = int(n**0.5) # n의 제곱근 구하는 것
    
    # 왜 제곱근까지만 체크하냐면 -> 약수는 대칭으로 이루어져서 2*6과 6*2 둘 다 동일
    for i in range(2, m+1):
        if prime[i]:
            # i이후부터 i의 배수는 다 소수가 아님
            for j in range(i+i, n+1, i):
                prime[j] = False
                
    for i in range(2, n+1):
        if prime[i]:
            answer += 1
    return answer