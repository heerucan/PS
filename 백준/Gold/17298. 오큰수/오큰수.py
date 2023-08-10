import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split(' ')))

answer = [-1]*n
stack = []

for i in range(len(a)):
    while stack and a[i] > stack[-1][0]:
        answer[stack[-1][1]] = a[i]
        stack.pop()
    stack.append((a[i],i))

for i in answer:
    print(i, end=' ')