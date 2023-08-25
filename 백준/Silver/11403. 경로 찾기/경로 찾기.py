import sys

input = sys.stdin.readline


def dfs(v):
    for i in range(n):
        if check[i] == 0 and arr[v][i] == 1:
            check[i] = 1
            dfs(i)


n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

check = [0 for _ in range(n)]

for i in range(n):
    dfs(i)
    print(*check)
    check = [0 for _ in range(n)]
