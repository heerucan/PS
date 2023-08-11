from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    truck = deque(truck_weights)
    time = 0
    sum_weight = 0
    
    while bridge:
        time += 1
        b = bridge.popleft()
        sum_weight -= b
        if truck:
            # 다리에 트럭을 더 올릴 수 있는 경우
            if sum_weight + truck[0] <= weight:
                t = truck.popleft()
                bridge.append(t)
                sum_weight += t
            else:
                bridge.append(0)
    return time