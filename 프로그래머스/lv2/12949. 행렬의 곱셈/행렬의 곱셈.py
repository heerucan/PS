def solution(arr1, arr2):
    # arr1의 행 * arr2의 열 = 행렬의 곱의 행과 열임
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    # [[0, 0], [0, 0], [0, 0]]
    # len(answer) - 행
    # len(answer[0]) - 열
    
    for i in range(len(arr1)): # 0 1 2
        for j in range(len(arr2[0])): # 0 1
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k]*arr2[k][j]
                # print(i, j ,k, answer)
            # print("----------")  
            
    return answer