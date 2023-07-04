# R : 배열의 수 순서 뒤집는 함수
# D : 첫 번째 수 버리는 함수
import sys
from collections import deque
t = int(sys.stdin.readline())

for _ in range(t):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    num = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    # num 배열을 받아서 양 괄호를 없애주고, , 단위로 분리해서 배열에 새로 넣어
    reverseBool = False

    if n == 0:
        num = []

    for i in p:
        # R이면 reverseBool의 값을 반대로 바꿔줌
        if i == 'R':
            reverseBool = not reverseBool
        elif i == 'D':
            if num: # 배열에 원소가 있는 경우
                if reverseBool: # 뒤집었음 -> 뒤 원소를 뺌
                    num.pop()
                else:
                    num.popleft()
            else: # 배열에 원소가 없는 경우
                num = 'error'
                break

    if num == 'error' or num == []:
        print(num)
    else:
        if reverseBool:
            num.reverse()
        print('[' + ','.join(num) + ']')
            

    # if num == 'error' or num == []:
    #     print('error')
    # elif num == ['']:
    #     print([])
    # else:
    #     if reverseBool:
    #         num.reverse()
    #     result = ','.join(num)
    #     print(f'[{result}]')