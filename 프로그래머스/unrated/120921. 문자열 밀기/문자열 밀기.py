def solution(A, B):
    if A == B:
        return 0
    else:        
        answer = 0
        tA,tB = list(A),list(B)
        while tA != tB:
            tA.append(tA.pop(0))
            answer += 1
            
            if answer == len(tA):
                answer = -1
                break
        
        answer = 0
        tA,tB = list(A),list(B)
        while tA != tB:
            tA.insert(0, tA.pop())
            answer += 1
            
            if answer == len(tA):
                answer = -1
                break
        
        return answer