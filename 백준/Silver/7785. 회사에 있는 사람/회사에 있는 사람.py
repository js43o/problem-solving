import sys

input = sys.stdin.readline

N = int(input())
s = set()

for _ in range(N):
    name, action = input().rstrip().split()
    if action == "enter":
        s.add(name)
    else:
        s.remove(name)

print(*sorted(list(s), reverse=True), sep="\n")
