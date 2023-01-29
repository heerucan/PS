from itertools import combinations
def solution(nums):
    answer = 0
    sumArr = []

    for x in combinations(nums, 3):
        sumArr.append(sum(x))
    
    # 배열에서 3개를 뽑아서 더한 후에, 
    # 해당 수를 1부터 자기자신까지 for문으로 나눠서 나눠떨어지는 값이 1, 자기자신인 것
    for i in sumArr:
        restArr = [] # 약수들의 배열
        for j in range(1, i+1):
            if i % j == 0:
                restArr.append(j)
        if len(restArr) == 2:
            answer += 1

    return answer