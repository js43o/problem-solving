import math, sys

while True:
    n = sys.stdin.readline().rstrip()
    if n == "0":
        break
    isCorrect = True
    for i in range(math.floor(len(n) / 2)):
        if n[i] != n[len(n) - 1 - i]:
            isCorrect = False
    print("yes" if isCorrect else "no")
