def solution(s):
    stackArr = []
    
    count = 0
    for i in s:
        if i == '(':
            stackArr.append(i)
            count += 1
        elif i == ')':
            if stackArr:
                stackArr.pop()
            count -= 1
            
    if not stackArr and count == 0:
        return True
    else:
        return False