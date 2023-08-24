import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
cube = []
q = deque()
MAX = 0
count = 0
day = 0
isAlreadyDone = True

for _ in range(H):
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    cube.append(matrix)

for h in range(H):
    for r in range(N):
        for c in range(M):
            if cube[h][r][c] != -1:
                MAX += 1
                if cube[h][r][c] == 1:
                    q.append([h, r, c, 0])
                    count += 1
                else:
                    isAlreadyDone = False


def bfs():
    global count
    global day

    while q:
        v = q.popleft()
        h, r, c, l = v[0], v[1], v[2], v[3]

        if l > day:
            day = l

        for vh, vr, vc in [
            [1, 0, 0],
            [-1, 0, 0],
            [0, 1, 0],
            [0, -1, 0],
            [0, 0, 1],
            [0, 0, -1],
        ]:
            if 0 <= h + vh < H and 0 <= r + vr < N and 0 <= c + vc < M:  # 범위 안에 있다면
                if cube[h + vh][r + vr][c + vc] == 0:  # 방문하지 않았다면
                    cube[h + vh][r + vr][c + vc] = 1
                    q.append([h + vh, r + vr, c + vc, l + 1])
                    count += 1


if isAlreadyDone:
    print(0)
else:
    bfs()
    if count < MAX:
        print(-1)
    else:
        print(day)
