# cards1,2의 주어진 순서대로 사용해야 함, card1 -> 2로 이동은 가능하나 각 배열에서 순서는 지켜야 함

def solution(cards1, cards2, goal):
    answer = ''
    sentence = []
    for g in goal:
        if cards1 and g == cards1[0]:
            sentence.append(cards1.pop(0))
        elif cards2 and g == cards2[0]:
            sentence.append(cards2.pop(0))
            
    if sentence == goal:
        return "Yes"
    else:
        return "No"