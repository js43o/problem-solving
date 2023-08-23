import sys


def last(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[len(arr) - 1]


n = int(input())
target = []
stack = []

for _ in range(n):
    target.append(int(sys.stdin.readline().rstrip()))

num = 1
index = 0
res = []
breaked = False

while index < n:
    if last(stack) < target[index]:
        stack.append(num)
        num += 1
        res.append("+")
    elif last(stack) == target[index]:
        stack.pop()
        res.append("-")
        index += 1
    else:
        breaked = True
        break

if not breaked:
    for i in res:
        print(i)
else:
    print("NO")
