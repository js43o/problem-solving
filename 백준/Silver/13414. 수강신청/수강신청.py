import sys

input = sys.stdin.readline

K, L = map(int, input().split())
tmplist = []
slist = []
sset = set()

for _ in range(L):
    s = input().rstrip()
    tmplist.append(s)

for s in reversed(tmplist):
    if s in sset:
        continue
    sset.add(s)
    slist.append(s)

print(*(list(reversed(slist))[:K]), sep="\n")
