import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
arr = []
queue = deque()  # 익은 토마토들의 좌표
num = 0  # 빈 자리 수와 익은 토마토 수의 합

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    arr.append(row)

    for j in range(M):
        if row[j] == -1 or row[j] == 1:
            num += 1
            if row[j] == 1:
                queue.append((i, j))

count = 0
diff = [(-1, 0), (0, -1), (1, 0), (0, 1)]

while len(queue) > 0:
    if num == M * N:
        break

    for _ in range(len(queue)):
        a, b = queue.popleft()
        for (x, y) in diff:
            if 0 <= a + x < N and 0 <= b + y < M:
                if arr[a + x][b + y] != 0:
                    continue
                arr[a + x][b + y] = 1
                num += 1
                queue.append((a + x, b + y))
    count += 1

if num == M * N:
    print(count)
else:
    print(-1)
