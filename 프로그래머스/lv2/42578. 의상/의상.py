# 종류 별 최대 1가지만 착용 가능
# 서로 다른 옷의 조합의 수 반환
# 해시에 {의상종류:개수}
# 최소 1개 의상은 입는다.
# 뭔가 의상종류: (개수, 의상) 이렇게 해주면 풀기 수월할 것 같음

from collections import defaultdict

def solution(clothes):
    answer = 1
    cloDict = defaultdict(list)
    for i in clothes:
        cloDict[i[1]].append(i[0])
        
    # {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}
    # headgear - 0X/X0/XX  eyewear - 0/X -> 곱하면 모든 경우의 수 -> 0X0/0XX/X00/X0X/XX0/XXX (XXX)는 빼줘야 함
    # {'face': ['crow_mask', 'blue_sunglasses', 'smoky_makeup']}
    # face - 0XX/X0X/XX0/XXX (XXX)는 빼야 함
    for value in cloDict.values():
        answer *= (len(value)+1)
    
    return answer-1