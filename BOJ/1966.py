# 중요도
# 중요도가 더 높은 문서가 현재 문서보다 있음 -> 큐의 가장 뒤로 현재문서 재배치
# 숫자가 클수록 - 높은 중요도

import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split(' ')) # n:문서개수 , m:현재 문서가 몇 번째에 있는지
    priorArr = deque(list(map(int, input().split(' '))))
    count = 0

    while priorArr:
        maxDoc = max(priorArr)
        if maxDoc == priorArr[0]:
            priorArr.popleft()
            count += 1
            if m == 0: # m 즉, 현재 문서가 가장 중요도가 높으면서 0번째 자리에 왔다는 뜻
                m = len(priorArr)-1
                print(count)
                break
            else:
                m -= 1
        else:
            priorArr.append(priorArr.popleft())
            if m == 0:
                m = len(priorArr)-1
            else:
                m -= 1
