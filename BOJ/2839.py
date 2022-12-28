n = int(input())

d = [-1] * 5001
d[3] = 1
d[5] = 1


for i in range(6, 5001):
    if i % 5 == 0:
        d[i] = d[i-5] + 1
    elif i % 3 == 0:
        d[i] = d[i-3] + 1
    elif d[i-3] > 0 and d[i-5] > 0:
        d[i] = min(d[i-3], d[i-5]) + 1
        

print(d[n])
