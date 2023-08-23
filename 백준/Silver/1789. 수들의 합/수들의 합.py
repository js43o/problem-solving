import sys

input = sys.stdin.readline

S = int(input())
count = 0
acc = 0

for i in range(1, S + 1):
    acc += i
    count += 1
    if acc >= S:
        if acc > S:
            count -= 1
        break

print(count)
