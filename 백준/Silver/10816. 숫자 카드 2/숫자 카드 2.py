# 10815랑 다르게 각 카드를 몇 개 가지고 있는지

import sys
input = sys.stdin.readline

from bisect import bisect_left
from bisect import bisect_right

n = int(input()) # 상근이가 갖고 있는 카드 개수
card_num = list(map(int, input().split())) # 상근이 숫자 카드 번호들
m = int(input()) 
check_num = list(map(int, input().split())) # 상근이 갖고 있는지 숫자인지 체크해야 할 정수

card_num.sort()

for i in check_num:
    left = bisect_left(card_num, i)
    right = bisect_right(card_num, i)
    if left == right:
        print(0, end=' ')
    else:
        if left > right:
            print(left - right, end=' ')
        else:
            print(right - left, end=' ')