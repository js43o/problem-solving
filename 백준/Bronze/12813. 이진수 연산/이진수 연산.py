import sys

input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
res = [[], [], [], [], []]

for i in range(len(A)):
    res[0].append(int(A[i]) & int(B[i]))
    res[1].append(int(A[i]) | int(B[i]))
    res[2].append(int(A[i]) ^ int(B[i]))
    res[3].append("1" if A[i] == "0" else "0")
    res[4].append("1" if B[i] == "0" else "0")

for r in res:
    print(*r, sep="")
