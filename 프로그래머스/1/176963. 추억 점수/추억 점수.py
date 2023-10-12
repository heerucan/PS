# yearning 추억점수
# 딕셔너리 사용
def solution(name, yearning, photo):
    answer = []
    grade = []
    
    for i in range(len(name)):
        grade.append([name[i], yearning[i]])
    
    dic = dict(grade)

    for i in photo:
        cnt = 0
        for j in i:
            if j in dic:
                cnt += dic[j]
        answer.append(cnt)
    
    return answer