import sys

N, M = map(int, input().split())
arr = {}

for i in range(1, N + 1):
    pokemon = sys.stdin.readline().rstrip()
    arr[i] = pokemon

arr_r = dict(map(reversed, arr.items()))

for _ in range(M):
    a = sys.stdin.readline().rstrip()
    if a[0] > "0" and a[0] <= "9":
        print(arr[int(a)])
    else:
        print(arr_r[a])
