def solution(word):
    words = []
    arr = ["A", "E", "I", "O", "U"]

    # n -> 5
    for i in arr:
        words.append(i)

    # n^2 -> 25
    for i in arr:
        for j in arr:
            words.append("".join(i+j))

    # n^3 -> 125
    for i in arr:
        for j in arr:
            for k in arr:
                words.append("".join(i+j+k))
    
    # n^4 -> 625
    for i in arr:
        for j in arr:
            for k in arr:
                for l in arr:
                    words.append("".join(i+j+k+l))

    # n^5 -> 3905 시간복잡도 ㄱㅊ
    for i in arr:
        for j in arr:
            for k in arr:
                for l in arr:
                    for m in arr:
                        words.append("".join(i+j+k+l+m))
    words.sort()
    
    return words.index(word)+1

solution("I")
