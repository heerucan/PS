# 1~n번 개인정보 n개
# 여러개의 약관 종류, 유효기간 있음, 기간 이후 파기
# 모든 달은 28일까지 존재
# 오늘 날짜 - today "YYYY.MM.DD"
# 약관의 유효기간 담은 1차원 문자열 배열 - term : 약관종류 + 유효기간 ["A 6", "B 12", "C 3"]
# 수집된 개인정보 담은 문자열 배열 - privacies : 개인정보 수집일자 + 약관종류 ["2021.05.02 A"]

# 출력값 : 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return

# 개인정보 수집 일자를 가지고 유효기간과 계산해 오늘날짜랑 비교해서 더 적으면 answer 배열에 넣어줌

def addZeroString(time):
    if time < 10:
        return ".0" + str(time)
    else: 
        return "." + str(time)

def calculateDate(arr, terms, type, year, month, day):
    for term in terms:
        termType, time = term.split(' ')
        if termType == type:
            # 유효기간을 12로 나눠서 몫은 년도, 나머지는 월로 더함
            totalMonth = month + int(time)
            if totalMonth > 12:
                year = year + totalMonth // 12
                if totalMonth % 12 == 0:
                    year -= 1
                    month = 12
                else:
                    month = totalMonth % 12
            else:
                month = totalMonth

            dueDate = str(year) + addZeroString(month) + addZeroString(day)
            arr.append(dueDate)
    return arr

def solution(today, terms, privacies):
    arr = []
    answer = []
    for privacy in privacies:
        day, type = privacy.split(" ")
        y, m, d = day.split(".")
        calculateDate(arr, terms, type, int(y), int(m), int(d))
        
    # 오늘 날짜랑 비교해서 오늘날짜랑 같거나 작으면 파기 -> answer로 넣기
    for i in range(len(arr)):
        if arr[i] <= today:
            answer.append(i+1)
    return answer

solution("2020.01.01", ["A 13"], ["2019.11.1 A"])

