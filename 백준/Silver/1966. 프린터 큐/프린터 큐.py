T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    priority = [0] * 10
    queue = list(map(int, input().split()))

    for i in queue:
        priority[i] += 1

    idx = 0
    count = 0
    isBreak = False
    for i in range(1, 10):
        while priority[10 - i] > 0:
            if idx == M and 10 - i == queue[M]:
                print(count + 1)
                isBreak = True
                break
            if queue[idx] == 10 - i:
                priority[10 - i] -= 1
                count += 1
            idx = (idx + 1) % len(queue)
        if isBreak:
            break
