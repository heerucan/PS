# 크기가 N인 수열A
# 수열의 각 원소에 대해서 오큰수를 구하기
# 오큰수 : 원소의 오른쪽에 있으면서 원소보다 큰 수 중 가장 왼쪽에 있는 수
# 없는 경우 -1

# a = [3,5,2,7] -> NGE(1)=5 / NGE(2)=7 / NGE(3)=7 / NGE(4)=7

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
aArr = deque(list(map(int, input().split())))
result = [-1]*n
stack = []

for i in range(n):
    while stack and aArr[stack[-1]] < aArr[i]:
        result[stack.pop()] = aArr[i]
    stack.append(i)

print(*result)