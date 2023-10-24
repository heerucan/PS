from string import ascii_lowercase

def solution(s, skip, index):
    answer = ''
    alpha = ascii_lowercase
    for i in skip:
        alpha = alpha.replace(i, "")
    length = len(alpha)
    
    for i in s:
        current = alpha.find(i)
        answer += alpha[(current+index)%length]
    return answer

