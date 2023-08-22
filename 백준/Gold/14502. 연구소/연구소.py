import sys, copy
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
mat = []
virus = []
result = 0

for i in range(N):
    arr = list(map(int, input().split()))
    mat.append(arr)
    for j in range(len(arr)):
        if arr[j] == 2:
            virus.append((i, j))


def bfs(mat):
    q = deque(virus)
    count = 0
    while q:
        y, x = q.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= y + dy < N and 0 <= x + dx < M and mat[y + dy][x + dx] == 0:
                mat[y + dy][x + dx] = 2
                q.append((y + dy, x + dx))

    for i in range(N):
        for j in range(M):
            if mat[i][j] == 0:
                count += 1

    return count


for i in range(N * M - 2):
    if mat[i // M][i % M] != 0:
        continue
    for j in range(i + 1, N * M - 1):
        if mat[j // M][j % M] != 0:
            continue
        for k in range(j + 1, N * M):
            if mat[k // M][k % M] != 0:
                continue
            mat[i // M][i % M] = 1
            mat[j // M][j % M] = 1
            mat[k // M][k % M] = 1
            result = max(result, bfs(copy.deepcopy(mat)))
            mat[i // M][i % M] = 0
            mat[j // M][j % M] = 0
            mat[k // M][k % M] = 0

print(result)
