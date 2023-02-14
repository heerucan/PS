def solution(s1, s2):
    answer = 0
    answer = len(list(set(s1).intersection(set(s2))))
    return answer