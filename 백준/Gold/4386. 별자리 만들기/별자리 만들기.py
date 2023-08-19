import sys
import math
import heapq

input = sys.stdin.readline

N = int(input())
pos = []
parent = [i for i in range(N)]
edges = []
res = 0


def getAncestor(k):
    if parent[k] == k:  # 내가 조상인가?
        return k
    return getAncestor(parent[k])


def setAncestor(k, a):
    stk = [k]
    while parent[k] != k:  # 자신의 모든 부모를 스택에 삽입
        stk.append(parent[k])
        k = parent[k]
    while stk:  # 그리고 전부 부모를 통일함
        parent[stk.pop()] = a


def union(k, l):
    k_ancestor = getAncestor(k)
    l_ancestor = getAncestor(l)
    if l_ancestor == k_ancestor:  # 이미 서로 union 되었다면 (조상이 같다면)
        return False
    setAncestor(l, k_ancestor)  # 조상 합치기
    return True


for i in range(N):
    x, y = map(float, input().split())
    pos.append((y, x))

for i in range(N - 1):
    y1, x1 = pos[i]
    for j in range(i + 1, N):
        y2, x2 = pos[j]
        d = math.sqrt(pow(y2 - y1, 2) + pow(x2 - x1, 2))
        heapq.heappush(edges, (d, i, j))

while len(edges) > 0:
    d, i, j = heapq.heappop(edges)
    if union(i, j):
        res += d

print(res)
