# 잘못된 수 부를 때마다 0을 외침 -> 지우도록 함
# 적은 수의 합을 알기 위함

import sys
input = sys.stdin.readline
k = int(input())

stackArr = []

for _ in range(k):
    integer = int(input())

    if integer == 0:
        stackArr.pop()
    else:
        stackArr.append(integer)

print(sum(stackArr))
