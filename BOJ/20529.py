# A~B + B~C + A~C : 세 사람의 심리적 거리

import sys
input = sys.stdin.readline
import itertools

# 조합 : 중복을 허용하지 않음

t = int(input())

def check(a, b):
    count = 0
    if a[0] != b[0]:
        count += 1
    if a[1] != b[1]:
        count += 1
    if a[2] != b[2]:
        count += 1
    if a[3] != b[3]:
        count += 1
    return count

for _ in range(t):
    n = int(input())
    mbti = list(input().rstrip().split(' '))
    if n > 32: 
        print(0)
    else:
        mbtiCombi = list(itertools.combinations(mbti, 3))
        temp = []
        for combi in mbtiCombi:
            one = combi[0]
            two = combi[1]
            three = combi[2]
            
            result = 0
            result += check(one, two)
            result += check(two, three)
            result += check(one, three)
            
            temp.append(result)
        print(min(temp))