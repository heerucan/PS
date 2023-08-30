import sys
input = sys.stdin.readline

# 나무수n, 집으로 가져갈 나무 길이m
n, m = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()

def bs(array, start, end, target):
    while start <= end:
        mid = (start+end)//2
        result = 0
        for i in array:
            if i > mid:
                result += i - mid
        if result >= target:
            start = mid + 1  
        else:
            end = mid - 1
    return end
        
print(bs(trees, 1, trees[n-1], m))