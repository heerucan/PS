# 양방향 순환 큐
# 왼쪽 이동 : 첫 원소가 맨 뒤로 이동
# 오른쪽 이동 : 맨 뒤 원소가 처음으로 이동

import sys
input = sys.stdin.readline
from collections import deque

# n : 큐의 크기, m : 뽑아내려고 하는 수의 개수
n, m = map(int, input().split(' '))
wantNum = deque(list(map(int, input().split(' '))))

queue = deque([i for i in range(1, n+1)])

# 무조건 앞에 있어야만 뽑을 수 있음
# 내가 원하는 숫자가 아니면 -> 2번 연산 (popleft -> append)
# 내가 원하는 숫자를 뒤에서 가져오려면 -> 3번 연산 (pop -> appendleft)
count = 0
while wantNum: # 내가 원하는 숫자를 다 뽑을 때까지
    if queue[0] == wantNum[0]: # 첫 번째 숫자가 내가 원하는 숫자
        queue.popleft()
        wantNum.popleft()
    elif queue[0] != wantNum[0]:
         # 찾고자 하는 값의 인덱스가 중간보다 뒤인 경우
        if queue.index(wantNum[0]) > len(queue)/2:
            # 3번 연산
            queue.appendleft(queue.pop())
            count += 1
        else: # 2번 연산
            queue.append(queue.popleft())
            count += 1
print(count)