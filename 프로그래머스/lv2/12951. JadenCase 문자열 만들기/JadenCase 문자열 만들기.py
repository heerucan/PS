# 문자열의 첫 문자를 대문자로 바꾸는 것 / 나머지는 소문자
# 만약 첫 문자가 숫자면 그냥 냅둘 것
def solution(s):
    result = ""
    is_new_word = True
    
    for char in s:
        if char == " ":
            is_new_word = True
            result += char
        elif is_new_word:
            result += char.upper()
            is_new_word = False
        else:
            result += char.lower()
    
    return result