# bridge_length : 다리에 최대 올라갈 수 있는 트럭이자, 다리 길이 : 2 -> 트럭에 2대 올라가고, 트럭도 2번 움직여야 내려온다.
# weight 이하까지의 무게 견딜 수 있음
# truck_weights : 트럭 별 무게

# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸림?
from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    truck = deque(truck_weights)
    time = 0
    
    while bridge:
        time += 1
        bridge.popleft()
        
        if truck:
            # 다리에 트럭을 더 올릴 수 있는 경우
            if sum(bridge) + truck[0] <= weight:
                t = truck.popleft()
                bridge.append(t)
            else:
                bridge.append(0)

    return time