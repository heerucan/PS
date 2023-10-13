def solution(X, Y):
    answer = ''

    for i in (set(X)&set(Y)): #중복을 제거하고 교집합을 찾아서
        #교집합의 원소가 X와 Y에 몇 개 있는지 체크하고 그 중 더 적게 있는 곳만큼 for문을 돌린다.
        for j in range(min(X.count(i), Y.count(i))): 
            answer += i
    
    if answer == "":
        return "-1"
    elif set(answer) == {"0"}:
        return "0"
    else:
        return "".join(sorted(answer, reverse=True))