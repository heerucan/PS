import sys
input = sys.stdin.readline

n = int(input()) # 상근이가 갖고 있는 카드 개수
card_num = list(map(int, input().split())) # 상근이 숫자 카드 번호들
m = int(input()) 
check_num = list(map(int, input().split())) # 상근이 갖고 있는지 숫자인지 체크해야 할 정수

card_num.sort()

def bs(array, start, end, target):
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
    result = bs(card_num, 0, n-1, i)
    if result == None:
        print(0, end=' ')
    else:
        print(1, end=' ')