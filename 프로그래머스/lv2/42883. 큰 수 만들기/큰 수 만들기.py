def solution(number, k):
    stack = []
    for i in number:
        while stack and i > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)
        
    while k > 0:
        stack.pop()
        k -= 1
            
    return ''.join(stack)