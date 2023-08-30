import sys
input = sys.stdin.readline

n = int(input())
a_nums = list(map(int, input().split()))
m = int(input())
check_num = list(map(int, input().split())) # 이 수들이 a_nums에 존재하는지 체크

a_nums.sort()

def binary_search(array, start, end, target):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

for i in check_num:
    result = binary_search(a_nums, 0, n-1, i)
    if result == None:
        print(0)
    else:
        print(1)