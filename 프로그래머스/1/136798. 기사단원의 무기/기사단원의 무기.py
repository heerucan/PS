# 기사단원 수 - number / 공격력의 제한수치 - limit / 제한수치 초가 기사의 무기 공격력 - power
def solution(number, limit, power):
    answer = 0
    little = [1]
    
    for n in range(2, number+1):
        cnt = 0
        for i in range(1, int(n**0.5)+1):
            if n / i == i:
                cnt += 1
            elif n % i == 0:
                cnt += 2
                
        little.append(cnt)
    
    for i in little:
        if i > limit:
            answer += power
        else:
            answer += i
            
    return answer