# 각 단어의 첫 번째 문자가 target 문자까지 가야 됨
# 최단거리 bfs 큐로 풀었지

from collections import deque

def solution(begin, target, words):
    answer = 0
    n = len(words)
    visited = [False] * n # 방문체크용 배열

    # 찾는 단어가 리스트에 없으면 0반환
    if target not in words:
        return 0

    queue = deque()
    queue.append([begin, 0]) # [첫 시작단어, 이동한 횟수(또는 깊이)]
    
    while queue:
        word, cnt = queue.popleft()
       
        # 만약 찾는 단어가 같으면 바로 멈춤
        if word == target:
            answer = cnt
            break 

        for i in range(n):
            temp_cnt = 0 # 다른 알파벳 개수 체크하기 위한 변수
            if not visited[i]: # 확인 안한 단어
                for j in range(len(word)):
                    # words 배열 속 단어와 다른 경우 한 자씩 비교해서 +1 
                    if word[j] != words[i][j]:
                        temp_cnt += 1

                # 만약 다른 알파벳 개수가 1개라면
                if temp_cnt == 1: 
                    # 큐에 해당 단어를 추가하고, (깊이+1) 추가
                    queue.append([words[i], cnt+1])
                    visited[i] = True # 방문처리

    return answer



solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])