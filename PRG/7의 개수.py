def solution(array):
    answer = 0
    newStr = []
    for i in array:
        if "7" in str(i):
            newStr += str(i).replace("7","칠")

    for i in newStr:
        if i == "칠":
            answer += 1
    
    return answer