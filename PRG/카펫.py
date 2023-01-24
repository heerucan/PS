def solution(brown, yellow):
    answer = []
    arr = []
    total = brown + yellow

    # total의 약수구하기 ex)48
    for i in range(1, total+1):
        if total % i == 0:
            arr.append(i)
            
    # 가로, 세로 추정해 (가로가 더 크거나 같은 경우만)
    # brown = (가로+세로)*2 - 4
    # yellow = total - brown
    for i in arr:
        for j in arr:
            if i >= j and (i+j)*2-4 == brown and i*j == total:
                answer.append(i)
                answer.append(j)            

    return answer

solution(24, 24)