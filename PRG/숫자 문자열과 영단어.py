# 숫자를 건네면, 영어로 바꿔서 전달 
# 우리는 원래 숫자를 찾아야 함

def solution(s):
    numDic = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 
     5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    
    for i in numDic:
        s = s.replace(numDic[i], str(i))
    answer = int(s)
    return answer

solution('one4seveneight')