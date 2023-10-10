def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    
    for i in range(len(babbling)):
        if "aya" in babbling[i]:
            babbling[i] = babbling[i].replace("aya", "1")
        if "ye" in babbling[i]:
            babbling[i] = babbling[i].replace("ye", "2")
        if "woo" in babbling[i]:
            babbling[i] = babbling[i].replace("woo", "3")
        if "ma" in babbling[i]:
            babbling[i] = babbling[i].replace("ma", "4")
    
    for i in babbling:
        if i.isdigit():
            if '11' not in i and '22' not in i and '33' not in i and '44' not in i:
                answer += 1
    return answer