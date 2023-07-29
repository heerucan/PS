# 스택을 사용한다! - 짝맞추는 것은 
def solution(s):
    answer = -1
    stack = []
        
    for i in range(len(s)):
        if not stack: # stack이 비어있으면 값을 넣어줘야 -> 비교할 수 
            stack.append(s[i])
        else:
            if stack[-1] == s[i]: #같으면
                stack.pop()
            elif stack[-1] != s[i]: #다르면
                stack.append(s[i])
    
    if stack: 
        answer = 0
    else: 
        answer = 1
            
    return answer