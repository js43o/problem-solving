import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [0] * 101
portal = [0] * 101

for _ in range(N):
    a, b = map(int, input().split())
    portal[a] = b

for _ in range(M):
    a, b = map(int, input().split())
    portal[a] = b


def bfs():
    q = deque([1])

    while q:
        v = q.popleft()

        # 뱀 또는 사다리가 있는 경우
        if portal[v] != 0:
            q.append(portal[v])
            matrix[portal[v]] = matrix[v]  # 방문 및 count 처리
        else:
            for i in range(1, 7):  # 주사위 굴리기
                if v + i <= 100 and (
                    matrix[v + i] == 0 or matrix[v] + 1 < matrix[v + i]
                ):
                    q.append(v + i)
                    matrix[v + i] = matrix[v] + 1


bfs()
print(matrix[100])
