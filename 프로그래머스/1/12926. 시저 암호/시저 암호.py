def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] != " ":
            if ord('a') <= ord(s[i]) <= ord('z') and ord(s[i])+n > ord('z'): #90
                answer += chr(64+ord(s[i])+n-ord('Z'))
                # print(answer, "1")
            elif ord('A') <= ord(s[i]) <= ord('Z') and ord(s[i])+n > ord('Z'): #122
                answer += chr(96+ord(s[i])+n-ord('z'))
                # print(answer, "2")
            else:
                answer += chr(ord(s[i])+n)
                
        elif s[i] == " ":
            answer += " "
    
    return answer