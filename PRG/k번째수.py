def solution(array, commands):
    answer = []
    for a in commands:
        arr = array[a[0]-1:a[1]]
        arr.sort()
        answer.append(arr[a[2]-1])
    return answer