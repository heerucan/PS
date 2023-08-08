from itertools import permutations
# 순서 상관있는 순열
# 에라토스테네스의 체 비슷한 문제
# 항상! 이런류의 문제는 is_prime 판별 메소드를 만들어서 풀 것!

def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0: 
            return False
    return True

def solution(numbers):
    answer = 0
    temp = []
    arr = []
    for i in range(1, len(numbers)+1):
        arr += list(permutations(numbers, i))
    
    noDuplicateArr = list(set(arr))
    for i in noDuplicateArr:
        newNum = int(''.join(i))
        if newNum not in temp and newNum > 1:
            temp.append(newNum)
     
    for i in temp:
        if is_prime(i):
            answer += 1
            
    return answer