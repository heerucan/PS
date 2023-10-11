# 2016/1/1 금요일 // 윤년
def solution(a, b):
    weeks = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    thirty = [1,3,5,7,8,10,12]
    days = b
    
    for i in range(1, a):
        if i in thirty:
            days += 31
        elif i == 2:
            days += 29
        else:
            days += 30
            
    return weeks[days%7]