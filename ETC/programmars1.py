# 당첨자수 >= 구매한사람수 -> 구매자 모두 당첨
# 당첨자수 < 구매한수 -> 무작위로 당첨자수만큼 당첨
# [당첨자수, 구매자수, 당첨금액]
# 가장 확률이 높은 복권을 사려고 함 -> 금액이 제일 높은 것
# 내가 사게 될 복권의 번호를 반환

def solutions(lotteries):
    answer = 0
    lottoDict = {} # 당첨금액: 인덱스
    perDict = {}
    dic = {} # 당첨금액:확률 추가한 딕셔너리

    for lotto in lotteries:
        getPercentage = lotto[0]/(lotto[1]+1)*100
        lottoDict[lotto[2]] = lotteries.index(lotto)+1
        perDict[getPercentage] = lotteries.index(lotto)+1
        dic[lotto[2]] = getPercentage
        
    cnt = 0
    for key,value in dic.items():
        if max(dic.values()) <= value:
            cnt += 1
        else:
            cnt += 0

    if cnt > 1:
        answer = lottoDict[max(lottoDict.keys())]
    else:
        answer = perDict[max(perDict.keys())]

    print(answer, cnt, dic)
    return answer