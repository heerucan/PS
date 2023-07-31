def solution(numbers):
    # numbers 각 원소를 문자열로 변경
    # lambda를 사용해서 각 원소를 3번씩 반복시켜주고, 내림차순 정렬
    # 1000 이하의 수라서 앞에서 3자리수끼리 비교하기 위함
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    
    # 00 -> 0으로 만들기 위한 식
    # cnt = 0
    # for i in numbers:
    #     if i == '0':
    #         cnt += 1
    # if len(numbers) == cnt:
    #     return '0'
    # else:
    #     return ''.join(numbers)
    
    # 위에 대신
    return str(int(''.join(numbers)))