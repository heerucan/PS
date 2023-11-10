# 순열로 만들 수 있는 옹알이 배열 만들고 있는지 체크
from itertools import permutations
def solution(babbling):
    answer = 0
    words = []
    main = ["aya", "ye", "woo", "ma"]
    for i in range(1,5):
        for j in permutations(main, i):
            words.append(''.join(j))
    
    for i in babbling:
        if i in words:
            answer += 1
    return answer