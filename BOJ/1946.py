# 서류, 면접이 둘 다 모두 떨어지면 선발X
# 신규 사원 채용 시 선발할 수 있는 신입 사원의 최대 인원수
import sys
t = int(input())

for i in range(t):
    n = int(input())

    people = [] # 신입사원 서류, 면접 점수 배열

    for i in range(n):
        people.append(list(map(int, sys.stdin.readline().split())))

    result = 0

    # 각 서류, 면접 순위가 더 낮아야 함
    # [[3, 2], [1, 4], [4, 1], [2, 3], [5, 5]]

    people.sort() # 서류 순서로 먼저 정렬

    minRank = people[0][1]

    for i in range(0, n):
        # 서류는 이미 정렬됐으니, 면접이 순위가 더 큰 경우만 카운팅해주면 됨
        if people[i][1] <= minRank:
            minRank = people[i][1]
            result += 1

    print(result)