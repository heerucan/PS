# 사용할 수 있는 정사각형 개수를 반환

def solution(w,h):
    answer = 0
    total = w*h
    # w, h의 최대공약수가 1이면 -> w+h-1 
    # 1보다 크면 -> w+h-최대공약수
    
    gcdArr = [] # 공약수 배열
    greatestValue = 0 # 최대공약수
    
    for i in range(min(w,h), 0, -1):
        if w % i == 0 and h % i == 0:
            gcdArr.append(i)
    
    greatestValue = gcdArr[0]
                
    if greatestValue == 1:
        answer = total-(w+h-1)
    elif w == h: # 정사각형의 경우
        answer = total-w
    elif greatestValue > 1:
        answer = total-(w+h-greatestValue)
    
    return answer

solution(8,12)