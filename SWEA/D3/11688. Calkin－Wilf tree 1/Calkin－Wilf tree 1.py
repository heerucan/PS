t = int(input())

for tc in range(1, t+1):
    node = input()
    root_a = 1
    root_b = 1
    for i in node:
        if i == 'L':
            root_a = root_a
            root_b = (root_a+root_b)
        elif i == 'R':
            root_a = (root_a + root_b)
            root_b = root_b

    print('#{}'.format(tc), root_a, root_b)
