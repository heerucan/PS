# 각 단어의 첫 번째 문자가 target 문자까지 가야 됨
# 최단거리 bfs 큐로 풀었지
# 2차원 배열

from collections import deque

def solution(begin, target, words):
    answer = 0
    n = len(words) # 그래프 길이
    visited = [False for _ in range(n)]

    # 만약 찾는 단어가 없으면 0
    if target not in words:
        return 0

    queue = deque()
    queue.append([begin, 0]) # 단어, 깊이

    while queue:
        word, cnt = queue.popleft()

        if word == target:
            answer = cnt
            break

        for i in range(0, n):
            temp_cnt = 0
            if not visited[i]: # 방문을 안한 경우
                for j in range(n): # 단어가 words 속 단어와 다를 때 비교
                    if word[j] != words[i][j]:
                        temp_cnt += 1

        if temp_cnt == 1: # 글자수가 1개 다르면
            queue.append([words[i], cnt+1])
            visited[i] = 1

    return answer



solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])