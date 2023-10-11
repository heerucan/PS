# 2016/1/1 금요일 // 윤년
def solution(a, b):
    answer = ''
    thirty = [1,3,5,7,8,10,12]
    feb = 2
    
    days = b
    
    for i in range(1,a):
        if i in thirty:
            days += 31
        elif i == feb:
            days += 29
        else:
            days += 30
            
    weeks = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    return weeks[days%7]
    
    # return answer