from collections import defaultdict

t = int(input())

for tc in range(1, t + 1):
    a = int(input())
    nums = list(map(int, input().split()))
    dic = defaultdict(int)
    score = [0] * 101

    for i in range(1000):
        score[nums[i]] += 1
    
    max_num = 0
    max_idx = 0
    for idx, value in enumerate(score):
        if max_num <= value:
            max_num = value
            max_idx = idx
    print('#{}'.format(tc), max_idx)