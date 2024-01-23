from collections import deque

# 원소 뽑기  -> 맨 앞 원소 삭제 popleft
# 왼쪽으로 이동 -> arr.append(arr.popleft())
# 오른쪽으로 이동 -> arr.appendleft(arr.pop())

# 큐크기 N / 뽑아낼 수 개수 M

# 반환할 것 : 2번, 3번 연산의 최솟값 반환

n, m = map(int, input().split(' '))
idxArr = deque(list(map(int, input().split(' '))))

# n크기의 큐 만들어
queue = deque()
for i in range(1,n+1):
    queue.append(i)

# 계산해줘야 함 . 왼쪽으로 돌리는게 나은지, 아니면 오른쪽이 더 나은지

res = 0
while idxArr:
    if idxArr[0] == queue[0]:
        queue.popleft()
        idxArr.popleft()
    else: # 다르면 방법을 선택해야 함
        # 찾고자 하는 숫자의 인덱스 구하기
        # 해당 숫자가 왼쪽에서 몇 칸
        # 해당 숫자가 오른쪽에서 몇 칸인지 체크

        left = queue.index(idxArr[0])
        right = len(queue)-1-left

        if left <= right:
            # 왼쪽이 더 작으면 2번 방법
            queue.append(queue.popleft())
            res += 1
        elif left > right:
            # 오른쪽이 더 작으면 3번 방법
            queue.appendleft(queue.pop())
            res += 1

print(res)