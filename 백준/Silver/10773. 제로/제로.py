import sys
from functools import reduce

n = int(input())
stack = []

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

print(reduce(lambda acc, cur: acc + cur, stack, 0))
