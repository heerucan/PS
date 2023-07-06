# VPS 즉, 올바른 괄호 짝이 제대로 잇는지 판단해서 YES, NO

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    count = 0
    stackArr = []
    bracket = list(input().rstrip())
    # 홀수면 애초에 NO
    if len(bracket)%2 != 0:
        print('NO')
    else: # 짝수들 중에서 체크
        for i in bracket:
            if i == '(':
                stackArr.append(i)
                count += 1
            elif i == ')':
                count -= 1
                if len(stackArr) != 0: # 배열에 ( 이 있는 경우만 pop
                    stackArr.pop()
        # 괄호 체크를 다했을 때, stackArr 배열이 비어있고, 괄호 짝도 개수가 올바르면 YES         
        if len(stackArr) == 0 and count == 0:
            print('YES')
        else:
            print('NO')