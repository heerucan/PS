import sys # 시간초과 때문에 해줘야 함!!

n, m = map(int, sys.stdin.readline().split())

# data = list(map(int, input().split())) 은 아래와 같음
data = list(map(int, sys.stdin.readline().split()))

# i번째 수 ~ j번째 수까지의 합
# D[n] = n번째 수까지의 합
D = [0] * 100000
a = 0
for i in range(0, n):
    a += data[i]
    D[i] += a

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    if i >= 2:
        print(D[j-1]-D[i-2])
    else:
        print(D[j-1])