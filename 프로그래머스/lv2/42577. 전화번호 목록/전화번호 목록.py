# 접두어면 false, 아니면 true
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if len(phone_book[i]) != len(phone_book[j]):
                if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                    return False
            else:
                break
            # if phone_book[i] != phone_book[j][:len(phone_book[i])] or :
            #     return True
            
    return True
