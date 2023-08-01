# 문자열의 첫 문자를 대문자로 바꾸는 것 / 나머지는 소문자
# 만약 첫 문자가 숫자면 그냥 냅둘 것
def solution(s):
    test_list = s.split(" ")
    result = []
    for i in test_list :
        result.append(i.capitalize())
    return ' '.join(result)