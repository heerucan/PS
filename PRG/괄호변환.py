def solution(p):
    answer = ''
    u = ''
    v = ''
    # 빈문자열이거나 올바른 괄호면 그대로 반환
    if checkBracket(p) == True or len(p) == 0:
        answer = p
    else:
        # 문자열 u(균형잡힌 문자열)/v로 쪼개기
        for i in range(2,len(p)+1,2):
            if checkBalance(p[:i]) == True:
                u = p[:i]
                v = p[i:]
                break
                
        # u가 올바른 괄호인 경우 
        if checkBracket(u) == True:
            answer = u + solution(v)
        else: # u가 올바르지 않은 경우
            # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
            # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
            # 4-3. ')'를 다시 붙입니다. 
            answer = '(' + solution(v) + ')'
            
            # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
            reverse = ''
            for j in u[1:-1]:
                if j == ')':
                    reverse += '('
                else:
                    reverse += ')'
            answer += reverse
    return answer

    
# 균형잡힌 괄호 체크
def checkBalance(p):
    check = 0
    for i in p:
        if i == "(":
            check += 1
        else:
            check -= 1
            
    if check == 0:
        return True
    else: return False
    
# 올바른 괄호인지 체크
def checkBracket(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if stack == []: # 오른쪽 괄호로 시작할경우
                return False
            else:
                stack.pop()
    if stack != []: # 다 끝났는데 왼쪽 괄호가 스택에 남아있을경우
        return False
    return True
