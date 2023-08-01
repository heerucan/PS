# n보다 큰 자연수
# n과, 큰 수는 2진수로 변환 시 1의 갯수가 같음
def solution(n):
    answer = 0
    binN = bin(n)[2:]
    oneCnt = binN.count('1')
    for i in range(n+1, 1000000):
        if bin(i)[2:].count('1') == oneCnt:
            answer = i
            break
        
    return answer