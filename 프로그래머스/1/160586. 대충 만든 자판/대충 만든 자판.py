def solution(keymap, targets):
    answer = []
    
    for target in targets:
        total = 0
        for alphabet in target:
            cnt = 0
            temp = []
            for keys in keymap:
                if keys.find(alphabet) != -1:
                    temp.append(keys.find(alphabet))
                elif keys.find(alphabet) == -1:
                    temp.append(1000)
            
            if temp and temp != [1000]:
                cnt += min(temp)+1
                total += cnt
            elif temp == [1000]:
                total += -10000

        if total <= -100 or total >= 1000:
            answer.append(-1)
        else:
            answer.append(total)        
        
    return answer


# print(solution(["ABCDE","ABBCE"], ["ABBEF"])) # [-1]
# print(solution(["FFF", "FFF"], ["CCC", "CCC"])) # [-1, -1]
# print(solution(["AGZ", "BSSS"], ["AGY", "BSSS"])) # [-1, 7]
# print(solution(["ABACD", "BCEFD"], ["XABCD", "AABB"])) # [-1, 4]