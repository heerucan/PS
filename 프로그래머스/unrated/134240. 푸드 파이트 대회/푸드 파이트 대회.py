def solution(food):
    answer = ''
    water = False
    if food[0] == 1:
        water = True
        
    for i in range(1, len(food)):
        if food[i] < 2: continue
        cnt = food[i]//2
        while cnt > 0:
            answer += str(i)
            cnt -= 1
            
    return answer + '0' + ''.join(reversed(answer))