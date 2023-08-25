import sys, math

heap = [0] * (100001 * 2 + 1)
num = 0

N = int(input())

for _ in range(N):
    oper = int(sys.stdin.readline().rstrip())
    if oper == 0:
        if num == 0:
            print(0)
        else:
            # 제거
            print(heap[1])
            heap[1] = heap[num]  # 마지막 원소를 가장 위로 올린다
            heap[num] = 0
            num -= 1

            # 힙 재정렬
            idx = 1
            while heap[idx] < heap[idx * 2] or heap[idx] < heap[idx * 2 + 1]:
                if heap[idx * 2] > heap[idx * 2 + 1]:
                    heap[idx], heap[idx * 2] = heap[idx * 2], heap[idx]
                    idx = idx * 2
                else:
                    heap[idx], heap[idx * 2 + 1] = heap[idx * 2 + 1], heap[idx]
                    idx = idx * 2 + 1
    else:
        # 삽입
        num += 1
        heap[num] = oper
        idx = num

        # 힙 재정렬
        while idx > 1 and heap[idx] > heap[math.floor(idx / 2)]:
            p = math.floor(idx / 2)
            heap[idx], heap[p] = heap[p], heap[idx]
            idx = p
