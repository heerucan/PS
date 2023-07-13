from collections import deque

def solution(progresses, speeds):
    answer = []
    progressQueue = deque(progresses)
    speedQueue = deque(speeds)
    
    day = 0
    count = 0
    while progressQueue:
        if progressQueue[0] + speedQueue[0]*day >= 100:
            progressQueue.popleft()
            speedQueue.popleft()
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            day += 1
    
    answer.append(count)
        
    return answer