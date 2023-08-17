import sys

input = sys.stdin.readline
carsBefore = []
carsAfter = []
beforeFront = {}
afterBack = {}
res = 0

N = int(input())
for i in range(N):
    s = input().rstrip()
    carsBefore.append(s)

for i in range(N):
    s = input().rstrip()
    carsAfter.append(s)

for i in range(N):
    beforeFront[carsBefore[i]] = set()
    afterBack[carsAfter[i]] = set()
    if i > 0:
        beforeFront[carsBefore[i]].update(carsBefore[:i])
    if i < N - 1:
        afterBack[carsAfter[i]].update(carsAfter[i + 1 :])

for car in carsBefore[1:]:
    bitten = beforeFront[car].intersection(afterBack[car])
    if len(bitten) > 0:
        res += 1

print(res)
