# 특정 프로세스가 몇 번째로 실행되는지 알아내기

# priorities : 프로세스 중요도
# location : 알고 싶은 프로세스의 위치
def solution(priorities, location):
    answer = 0
    
    indxArr = []
    for i in range(len(priorities)):
        indxArr.append(i)

    count = 0
    while priorities:
        maxVal = max(priorities)
        if priorities[0] == maxVal:
            priorities.pop(0)
            indx = indxArr.pop(0)
            count += 1
            if location == indx:
                answer = count
                break
        elif priorities[0] < maxVal:
            priorities.append(priorities.pop(0))
            indxArr.append(indxArr.pop(0))
            
    return answer