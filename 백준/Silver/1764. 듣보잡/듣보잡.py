import sys

N, M = map(int, input().split())
S1 = set()
S2 = set()

for _ in range(N):
    S1.add(sys.stdin.readline().rstrip())

for _ in range(M):
    S2.add(sys.stdin.readline().rstrip())

S = list(S1 & S2)
S.sort()

print(len(S))

for i in S:
    print(i)
