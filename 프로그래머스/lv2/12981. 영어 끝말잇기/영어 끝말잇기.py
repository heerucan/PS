# 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지
# 단어 중복인 경우, 탈락 / 끝 알파벳으로 시작하는 단어 안할 경우, 탈락

# 스택??
def solution(n, words):
    stack = []
    stack.append(words[0])
    
    for i in range(1, len(words)):
        if stack[-1][-1] == words[i][0] and words[i] not in stack: # 끝알파벳 == 시작알파벳
            stack.append(words[i])
        else:
            return [i%n+1, i//n+1]
    
    return [0,0]