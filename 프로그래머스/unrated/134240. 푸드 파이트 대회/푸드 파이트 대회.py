def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        cnt = food[i]//2
        while cnt > 0:
            answer += str(i)
            cnt -= 1
            
    return answer + '0' + ''.join(reversed(answer))