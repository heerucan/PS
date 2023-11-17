t = int(input())

for tc in range(1, t+1):
    word = input()
    alpha = ['a','e','i','o','u']
    new = ''
    for i in word:
        if i not in alpha:
            new += i

    print('#{}'.format(tc), new)
