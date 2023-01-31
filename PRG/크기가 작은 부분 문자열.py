def solution(t, p):
    answer = 0
        
    # 배열을 하나 만들고, p길이만큼 배열에 넣어서
    for i in range(len(t)):
        num = ""
        for j in list(t)[i:i+len(p)]:
            num += j
        # 만약 해당 숫자가 p보다 작거나 같고, p와 길이가 같은 경우만 +=1
        if int(num) <= int(p) and len(str(num)) == len(p):
            answer += 1
    
    return answer