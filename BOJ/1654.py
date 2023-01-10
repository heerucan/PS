# 이진탐색
# K개 랜선을 잘라서 N개 이상의 같은 길이의 랜선으로 만들기
# 자른 랜선은 붙일 수 없음
# 최대 랜선의 길이를 구하는 프로그램
# ex 300 -> 140, 140, 20(은 버림)

k, n = map(int, input().split())

data = []
for _ in range(k):
    data.append(int(input()))

data.sort() # 이진탐색은 정렬을 해줘야 쓸 수 있다. 

# x로 잘랐더니 n개 이상이 나왔다는 것은 x보다 작은 값으로 해도 n 이상이 나온다는 것.
# x로 자르면 n개 이상이 나옴? yes -> x를 증가시켜줘야 하고, no -> x를 감소시켜줘야 한다.


def binary_search(array, start, end, target):
    while start <= end:
        mid = (start+end) // 2
        value = 0
        for i in data:
            value += i//mid
            
        if value >= target:
            start = mid + 1        
        else:
            end = mid - 1

    return end

binary_search(data, 1, data[-1], n)