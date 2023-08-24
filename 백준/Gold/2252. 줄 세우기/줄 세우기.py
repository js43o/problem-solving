import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())
graph = [
    [set() for _ in range(2)] for _ in range(N + 1)
]  # graph[x][0] = 진입, graph[x][1] = 진출
q = deque()
res = []

for _ in range(M):
    A, B = map(int, input().split())
    graph[A][1].add(B)
    graph[B][0].add(A)

for i in range(1, N + 1):
    if len(graph[i][0]) == 0:
        q.append(i)

while q:
    v = q.popleft()
    res.append(v)

    for w in graph[v][1]:
        graph[w][0].remove(v)  # 관계 제거
        if len(graph[w][0]) == 0:  # 진입 차수가 0이 되었다면 큐에 추가
            q.append(w)

print(*res)
