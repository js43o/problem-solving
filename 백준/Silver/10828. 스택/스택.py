import sys

stack = []
n = int(input())

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        arg = command[1]
        stack.append(arg)
    elif command[0] == "pop":
        print(stack.pop() if len(stack) > 0 else -1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    elif command[0] == "top":
        print(stack[len(stack) - 1] if len(stack) > 0 else -1)
