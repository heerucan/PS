t = int(input())

for tc in range(1, t+1):
    a,b = map(int, input().split())
    res = 0
    if a >= 10 or b >= 10:
        res = -1
    elif a < 10 and b < 10:
        res = a*b

    print('#{}'.format(tc), res)
