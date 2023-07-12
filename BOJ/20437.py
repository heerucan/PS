import sys
input = sys.stdin.readline

from collections import defaultdict
# defaultdict은 딕셔너리인데 만약, 키에 대한 값이 없으면 값을 0으로 초기화해준다.

t = int(input())
for _ in range(t):
    w = input().rstrip() #문자열
    k = int(input()) #정수
    wDict = defaultdict(list)
    result = []

    for i, ch in enumerate(w):
        wDict[ch].append(i)

    print(wDict)
    
    # {'u': [1, 7], 'r': [4, 11], 'a': [5, 8, 13], 'o': [10, 15]}

    # ch 문자가 k번 이상인 것만 처리
    for ch, indices in wDict.items():
        if len(indices) >= k:
            for i in range(len(indices) - k + 1): # 딕셔너리 각 value 배열의 길이 - 1
                # indices = [1,7] ~ [10,15]
                # 7-1 / 11-4 / 8-5 / 13-8 / 15-10 을 해서 result에 추가
                result.append(indices[i+k-1] - indices[i]+1)

    if not result:
        print(-1)
    else:
        print(min(result), max(result))