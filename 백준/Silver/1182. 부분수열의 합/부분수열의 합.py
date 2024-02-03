from itertools import combinations

n, s = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
count = 0

for i in range(1, n+1):
    for j in combinations(data, i):
        # print("순열들: ", j, " / 합 = ", sum(j))
        if sum(j) == s:
            count += 1

print(count)