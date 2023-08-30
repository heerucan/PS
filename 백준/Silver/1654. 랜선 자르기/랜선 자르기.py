import sys
input = sys.stdin.readline

k, n = map(int, input().split())
line = [int(input()) for _ in range(k)]
line.sort()

def bs(array, start, end, target):
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        for i in array:
            cnt += i//mid

        # 만들어진 랜선개수가 필요한 개수보다 많으면 랜선길이를 늘려서 만들어질 개수를 줄여야 함
        if cnt >= target: 
            start = mid + 1
        else:
            end = mid - 1
    return end

print(bs(line, 1, line[k-1], n))