# anagrams를 할 수 있는 문자를 묶고, 그 배열의 개수를 반환

# 배열을 돌면서 서로 같으면 새로운 배열에 추가
# 배열 돌면서 cat의 각각 문자가 그 배열 내의 다른 단어들 속에 있는지 체크 + 문자열 길이도 같은지
from collections import defaultdict

def getGroupedAnagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        anagrams["".join(sorted(word))].append(word)

    anagramArr = list(anagrams.values())

    return len(anagramArr)

