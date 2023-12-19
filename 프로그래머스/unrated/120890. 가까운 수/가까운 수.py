def solution(array, n):
    array.append(n)
    array.sort()
    temp = []
    for i in range(0,len(array)):
        if n == array[i] and i == 0:
            return array[i+1]
        elif n == array[i] and i == len(array)-1:
            return array[i-1]
        elif n == array[i] and i != 0 and i != len(array)-1:
            temp.append(array[i-1])
            temp.append(array[i+1])
    
    if abs(temp[0]-n) > abs(temp[1]-n):
        return temp[1]
    else:
        return temp[0]