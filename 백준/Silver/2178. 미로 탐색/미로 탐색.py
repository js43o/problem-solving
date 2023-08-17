import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
matrix = []

for _ in range(N):
    matrix.append(list(sys.stdin.readline().rstrip()))

matrix[0][0] = 1  # 처음 칸 값을 정수형로 초기화


def bfs():
    q = deque([(0, 0)])
    while q:
        y, x = q.popleft()

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= y + dy < N and 0 <= x + dx < M:
                if y + dy == N - 1 and x + dx == M - 1:  # 마지막 칸 도착
                    print(matrix[y][x] + 1)
                    return

                if matrix[y + dy][x + dx] == "1":  # 처음 밟은 칸이면
                    matrix[y + dy][x + dx] = matrix[y][x] + 1  # 이전 칸 + 1 저장
                    q.append((y + dy, x + dx))


bfs()
