def solution(sizes):
    
    for i in sizes:
        if i[1] >= i[0]:
            temp = i[1]
            i[1] = i[0]
            i[0] = temp
    
    sizes.sort(reverse=True)

    a = max(sizes)[0]
    
    for i in sizes:
        if i[1] <= i[0]:
            temp = i[1]
            i[1] = i[0]
            i[0] = temp
            
    b = max(sizes)[0]
            
    return a*b