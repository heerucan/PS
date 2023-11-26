def solution(survey, choices):
    answer = ''
    rate = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    dic = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    select = []
    for i in range(len(choices)):
        if choices[i] < 4: # 왼쪽부분
            dic[survey[i][0]] += rate[choices[i]]
            
        elif 4 < choices[i]: #오른쪽부분
            dic[survey[i][1]] += rate[choices[i]]
            
    answer += check_type(dic,'R','T')
    answer += check_type(dic,'C','F')
    answer += check_type(dic,'J','M')
    answer += check_type(dic,'A','N')
    return answer

def check_type(dic,a,b):
    if dic[a] >= dic[b]:
        return a
    else:
        return b