import sys
input = sys.stdin.readline

import heapq

n = int(input())
temp = []
for _ in range(n):
    start, finish = map(int, input().split(' '))
    temp.append((start, finish))

temp.sort()

heap = []
heapq.heappush(heap, temp[0][1]) # 회의 끝나는 시간을 추가

for i in range(1, n):
    if heap[0] > temp[i][0]: # 1번회의 종료시간 > 2번회의 시작시간 : 회의실 필요
        heapq.heappush(heap, temp[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, temp[i][1])

print(len(heap))