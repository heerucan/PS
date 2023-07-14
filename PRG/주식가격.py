from collections import deque
def solution(prices):
    answer = []
    price = deque(prices)
    
    while price:  
        currentPrice = price.popleft()
        count = 0
        for nextPrice in price:
            count += 1
            if currentPrice > nextPrice: # 주식이 떨어진 경우
                break
        answer.append(count)
        
    return answer


# solution([1,2,3,2,3])
solution([1,2,3,2,3,1])
