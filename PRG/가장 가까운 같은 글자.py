def solution(s):
    answer = []
        
    for i in range(len(list(s))):
        if list(s)[i] in list(s)[0:i]:
            a = list(s)[i-1::-1]
            if list(s)[i] in a:
                answer.append(a.index(list(s)[i])+1)
        else:
            answer.append(-1)
        
    return answer


# 더 좋은 풀이
def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer