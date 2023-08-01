import sys
input = sys.stdin.readline

s = input().rstrip()
zero = s.count('0')//2
one = s.count('1')//2

answer = '0'*zero + '1'*one

answer = list(map(str, answer))
answer.sort()
print(''.join(answer))