def solution(quiz):
    answer = []
    for i in quiz:
        i = i.split(" ")
        res = 0
        if i[1] == '+':
            res = int(i[0])+int(i[2])
        elif i[1] == "-":
            res = int(i[0])-int(i[2])

        if res == int(i[4]):
            answer.append("O")
        else:
            answer.append("X")
            
    return answer