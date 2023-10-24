# 가장 좌상단 찾고, 가장 우하단을 찾기
# 좌상단 - x,y 모두 작은값 / 우하단 - x, y 모두 최댓값(각각+1해줘야 함)
def solution(wallpaper):
    tempX = []
    tempY = []
    for x, i in enumerate(wallpaper):
        for y, j in enumerate(i):
            if j == "#":
                tempX.append(x)
                tempY.append(y)
                    
    return [min(tempX), min(tempY), max(tempX)+1, max(tempY)+1]         