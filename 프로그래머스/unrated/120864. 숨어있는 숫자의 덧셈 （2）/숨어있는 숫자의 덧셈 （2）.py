from string import ascii_lowercase
def solution(my_string):
    answer = 0
    my_string = list(my_string.lower())
    
    for i in range(len(my_string)):
        if my_string[i] in ascii_lowercase:
            my_string[i] = ' '

    for i in ''.join(my_string).split(' '):
        if i != '':
            answer += int(i)
            
    if answer == 0:
        return 0
    else:
        return answer