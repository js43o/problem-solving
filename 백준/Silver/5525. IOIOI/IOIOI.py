N = int(input())
M = int(input())
S = input()
unit = 2 * N + 1


def isOk(idx):
    if idx + unit > M:
        return False
    for _ in range(N):
        if S[idx + 1] != "O" or S[idx + 2] != "I":
            return False
        idx += 2
    return True


count = 0
idx = 0

while idx <= M - unit:
    if S[idx] == "I" and isOk(idx):
        count += 1
    idx += 1

print(count)
