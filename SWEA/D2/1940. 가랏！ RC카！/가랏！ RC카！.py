t = int(input())

# 0 중지, 1 가속, 2 감속
for tc in range(1, t+1):
    n = int(input())
    speed = 0
    dis = 0

    for _ in range(n):
        command = list(map(int, input().split()))
        if command[0] == 1: # 가속
            speed += command[1]
        elif command[0] == 2:
            speed -= command[1]
            if speed < 0: # 현재 속도보다 감속할 속도가 더 크면 -> 속도는 0
                speed = 0

        dis += speed
    print('#{}'.format(tc), dis)