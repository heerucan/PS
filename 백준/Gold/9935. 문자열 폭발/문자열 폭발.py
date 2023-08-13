import sys
input = sys.stdin.readline

s = input().rstrip()
bomb = input().rstrip()
bomb_len = len(bomb)
# 스택을 사용해서 문자열을 다 넣어줘, 그리고 bomb 길이만큼 스택의 끝부분을 잘라서 bomb과 같으면 스택에서 제거해!

stack = []
for i in s:
    stack.append(i)
    if stack[-bomb_len:] == list(bomb):
        for i in range(bomb_len):
            stack.pop()

if ''.join(stack) == '':
    print('FRULA')
else:
    print(''.join(stack))