# 내림차순 정렬
# m개씩 앞에서부터 잘라
# 자른 배열마다 최소품질점수 * m개
def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    # score[0:3]
    # score[3:6]
    # score[6:9]
    # score[9:12]
    # score 개수 12 -> 3개씩 묶으면 4덩이가 나옴
    for i in range(0, int(len(score)/m)):
        splitArr = score[m*i:m*(i+1)]
        answer += splitArr[-1] * m

    return answer