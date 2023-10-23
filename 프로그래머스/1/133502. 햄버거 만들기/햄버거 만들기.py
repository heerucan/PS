# 1 2 3 1 이 되어야 햄버거 하나
def solution(ingredient):
    answer = 0
    
    if len(ingredient) < 4:
        return answer
    else:
        i = 0
        while i < len(ingredient) - 3:
            if ingredient[i:i+4] == [1,2,3,1]:
                ingredient[i:i+4] = []
                answer += 1
                i = 0
            else:
                i += 1
            
        return answer