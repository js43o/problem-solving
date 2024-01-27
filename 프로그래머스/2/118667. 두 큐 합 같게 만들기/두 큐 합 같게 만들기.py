def solution(queue1, queue2):
    count = 0
    q = queue1 + queue2
    start = 0
    end = len(queue1) - 1
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    while sum1 != sum2:
        if (start == 0 and end == len(queue1) - 1 and count > 0) or count > len(q) * 2:
            count = -1
            break
        
        if sum1 > sum2:
            if start == end:
                count = -1
                break
            
            sum1 -= q[start]
            sum2 += q[start]
            start = (start + 1) % len(q)
            count += 1
            continue
        
        if sum1 < sum2:
            if (end + 1) % len(q) == start:
                count = -1
                break
            
            end = (end + 1) % len(q)
            sum1 += q[end]
            sum2 -= q[end]
            count += 1
            continue

    return count