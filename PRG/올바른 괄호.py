from collections import deque

def solution(s):
    queue = deque()
    for i in list(s):
        queue.append(i)
        
    right = 0
    left = 0
    
    # 개수가 홀수 || ) .. ( || ( .. ( || ) .. ) 이면 false
    if len(queue) % 2 != 0 or queue[0] == ')' or queue[-1] == '(' or queue[0] == queue[-1]:
        return False
    else: # ( ... ) 인 경우들
        while queue: # queue가 빌 때까지 앞에서 하나씩 빼주면서 (,) 개수 카운팅
            l = queue.popleft() 
            if l == '(':
                right += 1
            else:
                left += 1
            # 근데 카운팅 도중에 ')'의 개수가 더 많으면 바로 false 날려줌
            # 여기서 '(' 개수가 더 많은 경우는 카운팅 안함 왜냐면, 어차피 얘가 더 많아도 후에 ')'가 있을 수 있으니까
            # ex.())(()과 같은 경우
            if right < left:
                return False
        # (,) 개수가 다르면 false -> ex.((()
        if right != left:
            return False
        else:
            return True