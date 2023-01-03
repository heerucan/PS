# 한 번에 한 명의 유저 신고
# 신고 횟수 제한X
# 서로 다른 유저                                                                                                                                                                                                                          계속 신고 가능
# 동일한 유저 신고 횟수는 1회로 처리
# k번 이상 신고 시 정지
# 전체 유저 목록이 ["muzi", "frodo", "apeach", "neo"]

# id_list : 이용자의 ID
# report : 유저가 신고한 ID
# k : 정지되는 신고 횟수
# 각 유저별로 처리 결과 메일을 받은 횟수 return 

# report 배열 [1]에 k번 이상 언급되면 신고되고, 
# 각 id_list의 result에 포함됨

# 중복 -> SET을 사용해!

def solution(id_list, report, k):
    answer = []
    userDict = {id: [] for id in id_list}
    resultDict = {id: 0 for id in id_list} 
    reportedUserDict = {id: 0 for id in id_list} 

    for i in set(report):
        a, b = i.split()
        
        userDict[a] += [b] # 신고한 사람
        reportedUserDict[b] += 1 # 신고당한 사람
    
    # 이중for문 낫베드...
    for i in reportedUserDict:
        for j in userDict:
            if reportedUserDict[i] >= k:
                if i in userDict[j]:
                    resultDict[j] += 1
    
    for i in resultDict:
        answer.append(resultDict[i])
    
    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)