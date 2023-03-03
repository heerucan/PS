# 각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"
# 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"
# 유저의 현재 피로도 k, ["최소 필요 피로도", "소모 피로도"] dungeons
# 유저가 탐험할수 있는 최대 던전 수를 return 

import sys
sys.setrecursionlimit(10**7)

def dfs(x, depth, visited, dungeons):
    for i in dungeons[x]:
        if x >= i[0] and not visited[i]:
            visited[i] = True
            dfs(x-i[0], depth+1, visited, dungeons)
            visited[i] = False

def solution(k, dungeons):
    # 방문처리 체크용 배열
    visited = [False]*len(dungeons)

    for i in range(len(dungeons)):
        if not visited[i]:
            visited[i] = True
            dfs(k, 0, visited, dungeons)
    

solution(80,[[80,20],[50,40],[30,10]])