import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
arr = deque([i for i in range(1, n+1)])

answer = []
count = 1
while len(arr) != 0:
    if count == k:
        answer.append(arr.popleft())
        count = 1
    else:
        arr.append(arr.popleft())
        count += 1    

stringList = list(map(str, answer))

print('<' + ', '.join(stringList) + '>')

