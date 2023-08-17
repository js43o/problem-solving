import sys

input = sys.stdin.readline

unit = [25, 10, 5, 1]
T = int(input())
for _ in range(T):
    C = int(input())
    count = [0, 0, 0, 0]
    for i in range(len(unit)):
        while C >= unit[i]:
            C -= unit[i]
            count[i] += 1
    print(*count)
