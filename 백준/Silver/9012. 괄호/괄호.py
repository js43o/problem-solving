import sys

n = int(input())

for _ in range(n):
    stack = []
    flag = True
    command = sys.stdin.readline().rstrip()
    for i in command:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                flag = False
                break
            stack.pop()
    print("YES") if (len(stack) == 0 and flag == True) else print("NO")
