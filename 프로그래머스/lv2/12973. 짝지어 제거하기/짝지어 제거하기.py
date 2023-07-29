# 스택을 사용한다! - 짝맞추는 것은 
from collections import deque

def solution(s):
    queue = deque()
        
    for i in range(len(s)):
        if not queue: # stack이 비어있으면 값을 넣어줘야 -> 비교할 수 있음
            queue.append(s[i])
        else:
            if queue[-1] == s[i]: #같으면
                queue.pop()
            elif queue[-1] != s[i]: #다르면
                queue.append(s[i])
    
    if queue: return 0
    else: return 1