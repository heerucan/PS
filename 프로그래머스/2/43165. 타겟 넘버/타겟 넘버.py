answer = 0
def solution(numbers, target):
    
    def backtracking(level, total):
        global answer
        if level == len(numbers): # 값이 같으면 반환
            if total == target:
                answer += 1
                return
        else: # 값이 안맞는 경우 - 백트래킹
            # 덧셈
            backtracking(level+1, total+numbers[level])
            # 뺄셈
            backtracking(level+1, total-numbers[level])
            
    backtracking(0,0)
    
    return answer