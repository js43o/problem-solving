import sys


M = int(input())
bit = 0

for _ in range(M):
    oper = sys.stdin.readline().split()
    if oper[0] == "all":
        bit = (1 << 20) - 1
    elif oper[0] == "empty":
        bit = 0
    else:
        oper, arg = oper[0], int(oper[1]) - 1
        if oper == "add":
            bit |= 1 << arg
        elif oper == "remove":
            bit &= ~(1 << arg)
        elif oper == "check":
            if bit & (1 << arg) == 0:
                print(0)
            else:
                print(1)
        elif oper == "toggle":
            bit = bit ^ (1 << arg)
