# 0 -> 알아볼 수 없는 번호
# 최고, 최저 순위를 배열로 반환
# 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums

def solution(lottos, win_nums):
    same = 0
    zero = 0
    high = 0
    
    # 일치:순위
    lottoDict = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}

    for i in lottos:
        # 내 배열 번호에 0이 몇 개인지 체크
        if i == 0:
            zero += 1
        # 내 배열 번호가 당첨 번호랑 몇 개가 같은지 체크해서 same 값에 담고
        if i in win_nums:
            same += 1
    
    # 최고 : 0개수 다 더하고 / 최저 : same       
    high = same + zero

    return [lottoDict[high], lottoDict[same]]