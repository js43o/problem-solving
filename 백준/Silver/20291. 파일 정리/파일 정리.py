import sys, itertools

input = sys.stdin.readline
extName = set()
extCount = {}

N = int(input())
for _ in range(N):
    _, ext = input().rstrip().split(".")
    extName.add(ext)
    if ext in extCount:
        extCount[ext] += 1
    else:
        extCount[ext] = 1

extList = sorted(list(extName))
for ext in extList:
    print("%s %s" % (ext, extCount[ext]))
