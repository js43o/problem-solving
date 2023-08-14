import sys

input = sys.stdin.readline


stk = []
N = int(input())

for _ in range(N):
    oper = input().rstrip()
    if oper[0] == "1":
        _, X = map(int, oper.split(" "))
        stk.append(X)
    if oper[0] == "2":
        print(stk.pop() if stk else -1)
    if oper[0] == "3":
        print(len(stk))
    if oper[0] == "4":
        print(0 if stk else 1)
    if oper[0] == "5":
        print(stk[-1] if stk else -1)
