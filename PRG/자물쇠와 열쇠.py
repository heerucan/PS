# 열쇠 = 2차원배열 key (회전과 이동이 가능)
# 자물쇠 = 2차원배열 lock
# 열 수 있으면 true, 없으면 false
# 홈은 0, 돌기는 1
# 완전탐색

# 2차원 리스트 90도 회전 함수
def rotate90(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            # 0,0 / 0,1 / 0,2 -> 0,2 / 1,2 / 2,2 
            result[j][n-i-1] = a[i][j]
    return result


# 자물쇠의 중간부분의 각 자리 값이 모두 1인지 확인하고 아니면 자물쇠와 키 안맞음
def check(newLock):
    # 3배 해줬으니까, 그 중간 부분에 박아준 자물쇠 부분을 구하기 위해서는 3으로 나누고
    # ex. 3~6 그 사이일 것임 그 사이 값들이 (키+자물쇠 = 1) => 맞아 떨어진다고 보면 됨
    lockLength = len(newLock) // 3
    for i in range(lockLength, lockLength*2):
        for j in range(lockLength, lockLength*2):
            if newLock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock) # 자물쇠크기
    m = len(key) # 키크기

    # 자물쇠의 크기를 기존보다 3배로 크게 변환
    newLock = [[0]*(n*3) for _ in range(n*3)]

    # 새로운 자물쇠의 중앙 부분에 기존 자물쇠를 박기
    for i in range(n):
        for j in range(n):
            # ex. 3,3 / 3,4 / 3,5 / ~ / 5,3 / 5,4 / 5,5
            newLock[i+n][j+n] = lock[i][j]

    # 4가지 방향에 대해 확인하기
    for rotation in range(4):
        # 열쇠 배열 90도 회전
        key = rotate90(key) 
        # x,y 범위는 0~5
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠 끼워넣기 m 범위는 0~2
                for i in range(m):
                    for j in range(m):
                        newLock[x+i][y+j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 들어가는지 검사 => 1이면 맞는 것
                if check(newLock) == True:
                    return True
                # 자물쇠에서 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        newLock[x+i][y+j] -= key[i][j]
    return False
