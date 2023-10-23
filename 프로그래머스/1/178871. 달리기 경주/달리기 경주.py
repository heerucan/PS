def solution(players, callings):    
    # 서로 스와핑하는 거
    # {말이름:등수}
    dic = {}
    for i in range(len(players)):
        dic[players[i]] = i
                   
    for i in callings:
        temp = i
        idx = dic[i]
        dic[i] = idx-1
        dic[players[idx-1]] = idx
        players[idx] = players[idx-1]
        players[idx-1] = temp
    return players