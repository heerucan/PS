survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

def solution(survey, choices):
    answer = ''
    dt = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}  # 답안참고
    choiceDt = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3} # 답안참고

    tester = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]

    for i in range(0, len(choices)):
        if choices[i] > 4:
            # print("오른쪽", survey[i][1], choices[i])
            dt[survey[i][1]] += choiceDt[choices[i]]
        elif choices[i] < 4:
            # print("왼쪽", survey[i][0], choices[i])
            dt[survey[i][0]] += choiceDt[choices[i]]

    for i in tester:
        if dt[i[0]] == dt[i[1]]:
            if i[0] < i[1]:
                answer += i[0]
            else:
                answer += i[1]
        elif dt[i[0]] > dt[i[1]]:
            answer += i[0]
        else:
            answer += i[1]

    # print(answer)
    return answer

solution(survey, choices)