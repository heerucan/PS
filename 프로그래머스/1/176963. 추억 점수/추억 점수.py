# yearning 추억점수
# 딕셔너리 사용
    
def solution(name, yearning, photo):
    answer = []
    
    dic = dict(zip(name, yearning))

    for i in photo:
        cnt = 0
        for j in i:
            if j in dic:
                cnt += dic[j]
        answer.append(cnt)
    
    return answer