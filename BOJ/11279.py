import heapq
import sys
input = sys.stdin.readline

n = int(input())
# x가 자연수면 x를 넣고
# x가 0이면 배열에서 가장 큰 값을 출력하고 그 값을 제거
heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if not heap: print(0)
        else:
            print(-heapq.heappop(heap))
    elif num > 0:
        # 부호를 바꿔서 넣어주고 -> heappop 후 다시 부호 바꿔줌
        heapq.heappush(heap, -num)