import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque([i for i in range(1, n+1)])
if n == 1:
    print(1)

while len(arr) != 1:
    for i in range(500000):
        if arr:
            if i%2 == 0: 
                arr.popleft()
            else: 
                arr.append(arr.popleft())

        if len(arr) == 1:
            print(arr[0])
            break