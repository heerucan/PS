import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

arr = deque()

for i in range(n):
    cal = input().rstrip().split(' ')

    if cal[0] == 'front':
        if not arr:
            print(-1)
        else:
            print(arr[0])
    elif cal[0] == 'back':
        if not arr:
            print(-1)
        else:
            print(arr[-1])
    elif cal[0] == 'size':
        print(len(arr))
    elif cal[0] == 'empty':
        if not arr: # 배열이 비어있는지 확인하는 것
            print(1)
        else:
            print(0)
    elif cal[0] == 'pop':
        if not arr:
            print(-1)
        else:
            print(arr.popleft())
    elif cal[0] == 'push':
        arr.append(cal[1])
