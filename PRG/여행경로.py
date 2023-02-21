
def solution(tickets):
    answer = []
    airport = []
    # 각 공항 별로 갈 수 있는 공항배열 만들기 
    for i in tickets:
        airport.append(i[0])
        airport.append(i[1])
    
    n = len(set(airport))
    
    graph = [[]*n]

    tickets.sort()
    for i in tickets:
        print(i)
    

    # for i in
    return answer

solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])