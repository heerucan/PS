
while True:
    strInput = input()
    stackArr = []
    count = 0

    if strInput == '.':
        break

    for i in strInput:
        if i == '(' or i == '[':
            stackArr.append(i)
            count += 1 
        elif i == ')':
            count -= 1
            if len(stackArr) != 0:
                if stackArr[-1] == '(':
                    stackArr.pop()
        elif i == ']':
            count -= 1
            if len(stackArr) != 0:
                if stackArr[-1] == '[':
                    stackArr.pop()

    if len(stackArr) == 0 and count == 0:
        print('yes')
    else:
        print('no')
