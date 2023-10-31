def solution(board):    
    # 개수 먼저 파악
    oCnt,xCnt = 0,0
    for i in board:
        oCnt += i.count("O")
        xCnt += i.count("X")
        
    # 승자가 없고, O >= X -> 올바름
    if oCnt < xCnt:
        return 0
    # 특정 개수가 2 이상으로 많을 때 -> O는 2개인데, X는 0개인 경우
    elif oCnt-xCnt > 1:
        return 0
    # O가 승자일 때, O == X+1 -> 올바름
    elif bingo(board,'O') and oCnt != xCnt+1:
        return 0
    # X가 승자일 때, O == X -> 올바름
    elif bingo(board,'X') and oCnt != xCnt:
        return 0
    # 둘 다 승자일 때 실패
    elif bingo(board,'O') and bingo(board,'X'):
        return 0
    
    return 1
       
def bingo(board,ox):
    # 대각선 빙고
    if board[0][0] == board[1][1] == board[2][2] == ox:
        return True
    if board[0][2] == board[1][1] == board[2][0] == ox:
        return True
    
    # 가로 빙고
    for i in board:
        if i.count(ox) == 3: 
            return True
    # 세로 빙고
    for i in range(3):
        cnt = 0
        for j in range(3):
            if board[j][i] == ox:
                cnt += 1
        if cnt == 3:
            return True
        
    return False