import heapq
import sys
input = sys.stdin.readline
n = int(input())

h = []
result = []
for i in range(n):
    x = int(input())
    if x == 0:
        if not h: # 빈 경우
            result.append((0,0))
        else: # 안 빈 경우 - 힙에서 빼기
            result.append(heapq.heappop(h))
    else:
        heapq.heappush(h, (abs(x),x))

for i in result:
    print(i[1])