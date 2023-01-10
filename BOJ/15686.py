# n*n 도시, 빈칸0/치킨집2/집1
# r,c (1,1)부터 시작 // (r1, c1)과 (r2, c2) 사이의 거리 = |r1-r2| + |c1-c2|
# 치킨거리 : 집에서 가장 가까운 치킨집 사이의 거리 (모든 집이 다 가짐)
# 도시의 치킨거리의 합 == 모든 집의 치킨 거리의 합

# 가장 수익 많이 내는 치킨집 수 = 최대 M개

# n : 도시 정보
# m : 폐업시키지 않을 치킨집의 최대값
# 출력값 : 도시의 치킨 거리의 최솟값

from itertools import combinations

n, m = map(int, input().split())

house = []
chicken = []
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

# 집, 치킨집 배열에 넣는 것임
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])


# 집을 하나씩 뽑아서 치킨 거리 구함
# 치킨집 최대 3개를 살린다 -> 전체에서 치킨집 3개 고르는 조합을 combinations로 구해

result = int(1e9) # 무한의 값을 result에 우선 넣음

# 고른 치킨집을 돌면서 집까지의 거리를 구함

for chickenStore in combinations(chicken, m):
    distance = 0 # 도시의 전체 치킨 거리
    for h in house:
        tempDistance = int(1e9) # 각 집마다 치킨 거리
        for j in range(m):
            xDistance = abs(h[0] - chickenStore[j][0])
            yDistance = abs(h[1] - chickenStore[j][1])
            tempDistance = min(tempDistance, xDistance+yDistance) # 더 짧은 치킨거리를 찾기
        distance += tempDistance # 도시 전체 치킨 거리를 구하기 위해 각 집까지의 치킨거리를 구해서 더함

result = min(result, distance) 
print(result)
