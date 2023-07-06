# push 오름차순

import sys
input = sys.stdin.readline

n = int(input())
stackArr = []
answer = []
smallerNum = 1
cannot = True

for _ in range(n):
    num = int(input())
    while smallerNum <= num:
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

