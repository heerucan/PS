t = int(input())

for tc in range(1, t+1):
    n = int(input())
    money = list(map(int, input().split()))
    res = 0
    avg = sum(money)/n
    for i in money:
        if i <= avg:
            res += 1

    print('#{}'.format(tc), res)
