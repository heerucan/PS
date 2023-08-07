# 뒤에 있는 수 + 자신보다 큼 + 가장 가깝게 있는 수
def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []

    for i in range(len(numbers)):
        while stack and stack[-1][0] < numbers[i]:
            answer[stack.pop()[1]] = numbers[i]
                        
        stack.append((numbers[i], i))
          
    return answer