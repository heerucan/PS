#완주하지 못한 선수 반환
#마라톤 참여 선수 - participant / 완주한선수 - completion
from collections import defaultdict

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    user_dic = defaultdict(int)
    for i in participant:
        user_dic[i] += 1
        
    for i in completion:
        user_dic[i] -= 1
    
    for key,value in user_dic.items():
        if value != 0:
            return key