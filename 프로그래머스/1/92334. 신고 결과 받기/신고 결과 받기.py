# 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.
# k번 이상 신고당해야 결과 메일 받음
# 그니까 각각의 유저가 신고한 ID가 k번 이상 신고 당했을 경우에만 정지시키는 것
# 각각의 유저가 신고한 ID가 정지된 계정에 포함됐을 경우만 발송
from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    user_dic = defaultdict(int) # 사용자별 신고당한 횟수
    report_dic = defaultdict(list) # 각각의 유저가 신고한 사용자ID
    reported_user = [] # k번 이상 신고당한 사용자
    
    temp_dic = defaultdict(int)

    for i in id_list:
        user_dic[i] = 0
        temp_dic[i] = 0
    
    for i in set(report):
        i = i.split(' ')
        user_dic[i[1]] += 1
        report_dic[i[0]].append(i[1])

    for key,value in user_dic.items():
        if value >= k:
            reported_user.append(key)
    
    for key,value in report_dic.items():
        cnt = 0
        for i in value:
            if i in reported_user:
                cnt += 1
        temp_dic[key] += cnt
    
    for value in temp_dic.values():
        answer.append(value)
    
    return answer