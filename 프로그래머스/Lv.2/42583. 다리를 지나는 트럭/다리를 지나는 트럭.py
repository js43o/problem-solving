from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    idx = 0
    bridge = deque([])
    curWeight = 0
    curCount = 0
    
    while idx < len(truck_weights):
        if len(bridge) == bridge_length:
            truckWeight = bridge.popleft()
            if truckWeight > 0:
                curWeight -= truckWeight
                curCount -= 1
        
        if curCount < bridge_length and curWeight + truck_weights[idx] <= weight:
            bridge.append(truck_weights[idx])
            curCount += 1
            curWeight += truck_weights[idx]
            idx += 1
        else:
            bridge.append(0)
            
        time += 1
    
    return time + bridge_length