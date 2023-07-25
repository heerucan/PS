# 완주하지 못한 선수를 반환
from collections import defaultdict
def solution(participant, completion):
    answer = ''
    
    # 동명이인을 밸류값에 몇 명인지 추가하자
    parDict = defaultdict(int) 
    for value in participant:
        parDict[value] += 1
    
    # {'mislav': 2, 'stanko': 1, 'ana': 1}
    
    for com in completion:
        parDict[com] -= 1
        
    for key, value in parDict.items():
        if value == 1:
            answer = key
    
    return answer