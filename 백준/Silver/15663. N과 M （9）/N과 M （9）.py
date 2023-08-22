import sys
from functools import reduce

input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

visited = [False] * N
result = {}
temp = []


def trav(count):
    if count == M:
        s = " ".join(map(str, temp))
        if s not in result:
            result[s] = 1
            print(s)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            temp.append(arr[i])
            trav(count + 1)
            temp.pop()
            visited[i] = False


trav(0)
