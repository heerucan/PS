def solution(answers):
    total = {1: 0, 2: 0, 3: 0}

    one = [1,2,3,4,5]*2000
    two = [2,1,2,3,2,4,2,5]*1300
    three = [3,3,1,1,2,2,4,4,5,5]*1000
    
    for i in range(len(answers)):
        answer = answers[i]
        if one[i] == answer:
            total[1] += 1
        if two[i] == answer:
            total[2] += 1
        if three[i] == answer:
            total[3] += 1
    
    # 딕셔너리를 정렬
    answer = []
    sortedTotal = dict(sorted(total.items()))

    k = max([sortedTotal[1], sortedTotal[2], sortedTotal[3]])

    if k == sortedTotal[1]:
        answer.append(1)
    if k == sortedTotal[2]:
        answer.append(2)
    if k == sortedTotal[3]:
        answer.append(3)

    return answer

solution([1,2,3,4,5,1,2,3,4,5])
