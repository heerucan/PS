# S에 시작해서 T에 끝나는 N개의 수업
# 최소의 강의실 사용해서 가능하게 하자
# 강의실 개수는?
import sys
input = sys.stdin.readline
import heapq

n = int(input())

q = []
for _ in range(n):
    s, t = map(int, input().split(' '))
    q.append([s, t])
q.sort()

endConference = []
heapq.heappush(endConference, q[0][1]) # 첫 회의 종료 시간을 넣어줌

for i in range(1, n):
    # 회의 끝나는 시간 > 그 다음 회의 시작 시간 -> 그 다음 회의방 추가
    if endConference[0] > q[i][0]:
        heapq.heappush(endConference, q[i][1])
    # 회의 끝나는 시간 <= 그 다음 회의 시작 시간 -> 기존 회의방을 빼고, 새로운 회의방 추가
    else:
        heapq.heappop(endConference) # 새로운 회의로 시간 변경을 위해 pop하고 새 시간 push
        heapq.heappush(endConference, q[i][1])

# 종료 시간이 빠른 회의방부터 다음 회의를 이어서 개최해야 해서, 우선순위 큐를 이용해 정렬을 유지
print(endConference)