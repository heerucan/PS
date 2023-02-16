
def solution(numbers):
    arr = []
    answer = ''
    answer1 = ''
    answer2 = ''

    
    # 각 숫자를 뒤집어서 arr에 추가 10 -> 01로 하는 과정
    for i in numbers:
        arr.append(str(i)[::-1])

    # print(arr) # 여기서 1차 만들어주고

    for i in arr:
        answer1 += ''.join(reversed(i))

    # arr를 오름차순으로 변경
    reverseArr = sorted(arr, reverse = True) # 여기서 2차로 만들었을 때 각각 비교

    # reverseArr에서 뒤집힌 숫자를 뽑아서 answer에 추가
    for i in reverseArr:
        answer2 += ''.join(reversed(i))

    answer = [answer1, answer2]
    print(answer)


    if list(set(arr))[0] == '0' and len(set(arr)) == 1:
        print('0')
        return 0
    else:
        print(max(answer))
        return max(answer)


solution([30, 3021])
solution([12, 1213])
solution([3, 30, 34, 5, 9])
solution([212,21])
solution([70,0,0,0,0])
solution([0,0,0,0])
# solution([1, 10, 100, 100, 818, 81, 898, 89, 0, 0])
