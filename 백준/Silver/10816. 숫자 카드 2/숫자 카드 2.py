import sys, math

n = int(input())
ns = [0] * 20000001
for i in list(map(int, sys.stdin.readline().split())):
    ns[i + 10000000] += 1

m = int(input())
ms = [str(ns[i + 10000000]) for i in list(map(int, sys.stdin.readline().split()))]

print(" ".join(ms))
