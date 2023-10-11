# a개 가져다주면 b병 주는 마트
# 단, 보유 중인 빈 병이 2개 미만이면 안됨

# a - 마트에 줘야 하는 빈 병, b - 마트가 주는 병 개수, n - 상빈이가 갖고 있는 병 개수
def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += n//a*b
        n = n - n//a*a + n//a*b
    return answer