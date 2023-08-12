import sys
input = sys.stdin.readline

n = int(input())
square = []
for _ in range(n):
    square.append(list(map(int, input().split(' '))))

# [[2, 4], [11, 4], [15, 8], [4, 6], [5, 3], [8, 10], [13, 6]]

square.sort()
max_square = max(square, key=lambda x: x[1])
max_index = square.index(max_square)

result = 0
height = square[0][1]

for i in range(max_index):
    if height < square[i+1][1]:
        result += (square[i+1][0]-square[i][0])*height
        height = square[i+1][1]
    else:
        result += (square[i+1][0]-square[i][0])*height

height = square[-1][1]
for i in range(n-1, max_index, -1):
    if height < square[i-1][1]:
        result += (square[i][0]-square[i-1][0])*height
        height = square[i-1][1]
    else:
        result += (square[i][0]-square[i-1][0])*height

print(result+max_square[1]*1)