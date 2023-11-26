#둘다 일치 login / 아이디일치 wrong pw / 아이디불일치 fail
def solution(id_pw, db):
    answer = ''
    id,pw = id_pw[0], id_pw[1]
    if id_pw in db:
        return 'login'
    for dbs in db:
        if id == dbs[0] and pw != dbs[1]:
            answer = 'wrong pw'
        elif id != dbs[0] and pw != dbs[1]:
            answer = 'fail'
    
    return answer