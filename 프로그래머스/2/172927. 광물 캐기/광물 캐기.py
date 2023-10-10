# 곡괭이 개수 picks, 광물들의 순서 minerals
# 마인이 작업을 끝내기까지 필요한 최소한의 피로도 반환
# 곡괭이 하나 선택해서 광물 5개 연속으로 캐고, 다음 곡괭이를 선택해서 광물 5개 캐기 반복
# 철곡 -> 다이아 5 / 돌곡 -> 다이아 25 / 돌곡 -> 철 5 / 나머지 1
# 그니까 picks에서 곡괭이를 꺼내서 총 5번 사용할 수 있음 (광물순서대로)
# 대신 picks에서는 맘대로 곡괭이 순서상관없이 사용 가능
# 그러면, minerals의 종류를 보고 곡괭이를 선택해야 함

def solution(picks, minerals):
    answer = 0
    sum = 0
    # 곡괭이의 수를 구한다.
    for i in picks:
        sum += i
    
    # 전체곡괭이 개수로 캘 수 있는 광물만큼 자른다.
    # 만약 전체가 6개면 총 30개만 캘 수 있으니까 만약 minerals 개수가 35면 30개까지 컷해준다.
    num = sum * 5
    if len(minerals) > sum:
        minerals = minerals[:num]
    
    # 광물들을 조사한다.
    new_minerals = []
    # 만약 minerals가 8개면 하나의 곡괭이로 5번씩 캘 수 있으니까, 총 두 번 루프를 돌아서 광물을 캐줘야 함
    for _ in range((len(minerals)//5 + 1)):
        new_minerals.append([0,0,0])
        # [[0, 0, 0], [0, 0, 0]]
    
    # new_minerals의 각 배열은 총 광물 5개까지만 가능해서, 그렇게 쪼개준 것임 [[3, 2, 0], [1, 1, 1]]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            new_minerals[i//5][0]+=1
        elif minerals[i] == 'iron':
            new_minerals[i//5][1]+=1
        elif minerals[i] == 'stone':
            new_minerals[i//5][2]+=1
            
    # 광물의 순서를 다이아몬드, 철, 돌 순서대로 정렬해준다.
    # 정렬을 하는 이유
    new_minerals.sort(key=lambda x:(-x[0],-x[1],-x[2]))
    
    # 정렬된 광물들을 다이아,철,돌 곡괭이 순서대로 캔다.
    for i in new_minerals:
        dia,iron,stone = i
        for j in range(len(picks)): # 곡괭이 다 쓸 때까지 돌려줘
            if picks[j]>0 and j==0: #다이아곡괭
                picks[j]-=1
                answer += dia + iron + stone
                break
            elif picks[j]>0 and j==1: #철곡괭
                picks[j]-=1
                answer += (5*dia) + iron + stone
                break
            elif picks[j]>0 and j==2: #돌곡괭
                picks[j]-=1
                answer += (25*dia) + (5*iron) + stone
                break
    return answer