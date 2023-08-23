import sys

input = sys.stdin.readline


def getScore(n):
    return 1 if n % 2 != 0 else 0


M = input().rstrip()
resMax = 0
resMin = 0


def getResult(N, mode):
    res = 0
    while True:
        for n in N:
            res += getScore(int(n))
        if len(N) <= 1:
            break
        if len(N) == 2:
            N = str(int(N[0]) + int(N[1]))
            continue
        tmpRes = 0 if mode == "MAX" else 10**20
        tmpN = None
        for i in range(1, len(N) - 1):
            for j in range(i + 1, len(N)):
                newN = int(N[:i]) + int(N[i:j]) + int(N[j:])
                r = getResult(str(newN), mode)
                if (mode == "MAX" and r >= tmpRes) or (mode == "MIN" and r <= tmpRes):
                    tmpRes = r
                    tmpN = str(newN)
        N = tmpN
    return res


print(getResult(M, "MIN"), getResult(M, "MAX"))
