# push 오름차순

import sys
input = sys.stdin.readline

n = int(input())
stackArr = []
answer = []
smallerNum = 1
cannot = True # 오름차순으로 POP할 수 없어서 NO를 출력해줘야 할 경우 사용하는 것

for _ in range(n):
    num = int(input())
    while smallerNum <= num: # 4를 pop하기 위해 그 전 수를 push하기 위한 while문
        stackArr.append(smallerNum)
        answer.append('+')
        smallerNum += 1
        
    if stackArr[-1] == num:
        stackArr.pop()
        answer.append('-')
    else:
        print('NO')
        cannot = False
        break

if cannot:
    for i in range(len(answer)):
        print(answer[i])

