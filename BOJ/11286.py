import heapq
import sys
input = sys.stdin.readline

# 배열에 정수 (0 제외)를 넣음

# 절댓값이 가장 작은 값이 여러개면, 가장 작은 수를 출력하고 배열에서 제거

n = int(input())
heap = []

temp = []

for _ in range(n):
    num = int(input())
    if num != 0:
        # 절댓값, 원래값을 넣어서 절댓값 기준으로 정렬
        heapq.heappush(heap, (abs(num), num)) 
    elif num == 0:
        if not heap: temp.append((0,0))
        else:
            temp.append(heapq.heappop(heap))

for i in temp:
    print(i[1])