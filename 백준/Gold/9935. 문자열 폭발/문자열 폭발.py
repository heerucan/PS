import sys
input = sys.stdin.readline

strings = input().rstrip()
bomb = input().rstrip()

# 스택을 만들어서 bomb 문자 길이가 될 때까지 순회하며 넣다가, 만약 스택의 문자가 bomb과 같은 경우 
# 스택에서 bomb 문자 길이만큼 pop해준다.

stack = []
bomb_len = len(bomb)

for i in range(len(strings)):
    stack.append(strings[i])  
    if ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
