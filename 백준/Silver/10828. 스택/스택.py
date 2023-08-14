
import sys
n = int(sys.stdin.readline())

stackArray = []

def push(array, x):
    return array.append(x)

def pop(array):
    if len(array) == 0:
        print(-1)
    else:
        n = array.pop(-1)
        print(n)

def size(array):
    print(len(array))

def empty(array):
    if len(array) == 0:
        print(1)
    else:
        print(0)

def top(array):
    if len(array) == 0:
        print(-1)
    else:
        print(array[-1])

for _ in range(n):
    cal = sys.stdin.readline().rstrip()

    if cal == 'pop':
        pop(stackArray)
    elif cal == 'size':
        size(stackArray)
    elif cal == 'empty':
        empty(stackArray)
    elif cal == 'top':
        top(stackArray)
    elif 'push' in cal:
        val = cal.split(' ')
        push(stackArray, val[1])
