import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [set() for _ in range(N + 1)]
in_deg = [0] * (N + 1)
res = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].add(B)
    in_deg[B] += 1

for counter in range(1, N + 1):
    target = []  # 한꺼번에 간선 제거를 위해 모아두기

    for p in range(1, N + 1):
        if in_deg[p] == 0:
            target.append(p)

    for p in target:
        in_deg[p] = -1  # 방문 처리
        res[p] = counter
        for q in graph[p]:
            in_deg[q] -= 1

print(*res[1:])
