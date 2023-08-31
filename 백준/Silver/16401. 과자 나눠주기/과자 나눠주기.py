from sys import stdin
input = stdin.readline

m, n = map(int, input().split())
lengths = list(map(int, input().split()))

lengths.sort()

def bs(array, start, end, target):
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        for i in array:
            if i >= mid:
                cnt += i//mid
        if cnt >= target:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(bs(lengths, 1, lengths[-1], m))