from itertools import permutations
# 순서 상관있는 순열

def solution(numbers):
    answer = 0
    temp = []
    a = []
    for i in range(1, len(numbers)+1):
        a = list(permutations(numbers, i))
        for i in a:
            newNum = int(''.join(i))
            if newNum > 1 and newNum not in temp:
                if newNum == 2:
                    temp.append(newNum)
                elif newNum % 2 != 0:
                    temp.append(newNum)
                
    for i in temp:
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt == 2:
            answer += 1
            
    return answer