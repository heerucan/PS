def solution(players, callings):    
    # {이름:등수}
    dic = {}
    for idx, val in enumerate(players):
        dic[val] = idx
                   
    for i in callings:
        idx = dic[i]
        dic[i] -= 1 #추월하는 선수 등수-1
        dic[players[idx-1]] = idx #추월당한 선수 = 추월하는 선수의 기존 등수 (idx) 
        
        # players에서 스와핑
        players[idx], players[idx-1] = players[idx-1], i
        
    return players