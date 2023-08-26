import sys

input = sys.stdin.readline

N = input().rstrip()
arr = list(list(N))
arr.sort(reverse=True)
result = int("".join(arr))

print(result if result % 30 == 0 else -1)
