# 점수개수 k // 마지막날까지 출연한 가수 점수들 score
# 매일 발표된 최하위 점수를 반환

def solution(k, score):
    answer = []
    fame_board = []
            
    if k >= len(score):
        for i in range(len(score)):
            fame_board.append(score[i])
            fame_board.sort()
            answer.append(fame_board[0])
    else:
        for i in range(k):
            fame_board.append(score[i])
            fame_board.sort()
            answer.append(fame_board[0])

        for i in range(k, len(score)):
            if fame_board[0] < score[i]:
                min = fame_board.pop(0)
                fame_board.append(score[i])
                fame_board.sort()
            answer.append(fame_board[0])
    
    return answer