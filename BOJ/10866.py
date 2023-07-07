import sys
input = sys.stdin.readline

from collections import deque

arr = deque()

n = int(input())
for _ in range(n):
    cal = input().rstrip().split(' ')
    if cal[0] == 'push_front':
        arr.appendleft(cal[1])
    elif cal[0] == 'push_back':
        arr.append(cal[1])
    elif cal[0] == 'pop_front':
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif cal[0] == 'pop_back':
        if arr:
            print(arr.pop())
        else:
            print(-1)
    elif cal[0] == 'size':
        print(len(arr))
    elif cal[0] == 'empty':
        if arr: print(0)
        else: print(1)
    elif cal[0] == 'front':
        if arr: print(arr[0])
        else: print(-1)
    elif cal[0] == 'back':
        if arr: print(arr[-1])
        else: print(-1)

