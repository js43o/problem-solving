import heapq, sys


def solution(operations):
    maxArr = []
    minArr = []
    exist = {}

    for oper in operations:
        cmd, num = oper.rstrip().split(" ")
        num = int(num)
        if cmd == "I":
            heapq.heappush(minArr, num)
            heapq.heappush(maxArr, -num)
            if num in exist:
                exist[num] += 1
                continue
            exist[num] = 1
        elif cmd == "D":
            if num == 1:
                while len(maxArr) > 0 and exist[-maxArr[0]] == 0:
                    heapq.heappop(maxArr)
                if len(maxArr) > 0:
                    removed = -heapq.heappop(maxArr)
                    exist[removed] -= 1
            elif num == -1:
                while len(minArr) > 0 and exist[minArr[0]] == 0:
                    heapq.heappop(minArr)
                if len(minArr) > 0:
                    removed = heapq.heappop(minArr)
                    exist[removed] -= 1

    # 최종 동기화
    while len(maxArr) > 0 and exist[-maxArr[0]] == 0:
        heapq.heappop(maxArr)

    while len(minArr) > 0 and exist[minArr[0]] == 0:
        heapq.heappop(minArr)

    if len(maxArr) == 0 or len(minArr) == 0:
        return [0, 0]
    return [-maxArr[0], minArr[0]]


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    operations = []
    for _ in range(k):
        operations.append(input().rstrip())
    res = solution(operations)
    if res == [0, 0]:
        print("EMPTY")
        continue
    print("%s %s" % (res[0], res[1]))
