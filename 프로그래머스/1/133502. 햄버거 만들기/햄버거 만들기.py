# 1 2 3 1 이 되어야 햄버거 하나
def solution(ingredient):
    answer = 0
    temp = []
    for i in ingredient:
        temp.append(i)
        if temp[-4:] == [1, 2, 3, 1]:
            answer += 1
            temp.pop()
            temp.pop()
            temp.pop()
            temp.pop()
            continue  # 다시 패턴 찾기 시작
    return answer