from collections import deque

def solution(bridge_length, weight, truck_weights):
    sec = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    curr_weight = 0

    while bridge:
        sec += 1
        curr_weight -= bridge.popleft()

        if truck_weights:
            if curr_weight + truck_weights[0] <= weight:
                tw = truck_weights.popleft()
                bridge.append(tw)
                curr_weight += tw
            else:
                bridge.append(0)  # 무게 넘으면 weight가 0인 트럭이 간다고 생각하고 채움

    return sec