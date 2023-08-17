import sys

input = sys.stdin.readline

N = int(input())
cards = set(list(map(int, input().split())))
M = int(input())
checks = list(map(int, input().split()))

for i in range(len(checks)):
    checks[i] = 1 if checks[i] in cards else 0

print(*checks)
