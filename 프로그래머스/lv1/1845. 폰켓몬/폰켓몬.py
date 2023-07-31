# N마리 폰켓몬 중 N/2마리를 골라야 하는데, 종류는 제일 다양해야 해! -> 종류를 return
def solution(nums):
    n = int(len(nums)/2)
    nums = set(nums)
    
    if n >= len(nums):
        return len(nums)
    else:
        return n
