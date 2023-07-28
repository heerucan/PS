def dfs(k, cnt, dungeons, visited, answer):
    for i in range(len(dungeons)):
        if not visited[i] and dungeons[i][0] <= k:
            visited[i] = True
            answer = dfs(k-dungeons[i][1], cnt+1, dungeons, visited, answer)
            visited[i] = False
    return max(answer, cnt)
            
def solution(k, dungeons):
    visited = [False]*len(dungeons)
    answer = dfs(k, 0, dungeons, visited, 0)
    return answer