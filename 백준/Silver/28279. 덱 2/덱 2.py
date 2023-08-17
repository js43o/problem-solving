import sys

input = sys.stdin.readline

size = 2000001
mem = [None] * size
front = 1000000
rear = 1000001


def isEmpty():
    return front + 1 == rear


N = int(input())
for _ in range(N):
    oper = input().rstrip().split()
    if oper[0] == "1":
        num = int(oper[1])
        mem[front] = num
        front -= 1
    if oper[0] == "2":
        num = int(oper[1])
        mem[rear] = num
        rear += 1
    if oper[0] == "3":
        if not isEmpty():
            front += 1
            print(mem[front])
        else:
            print(-1)
    if oper[0] == "4":
        if not isEmpty():
            rear -= 1
            print(mem[rear])
        else:
            print(-1)
    if oper[0] == "5":
        print(rear - front - 1)
    if oper[0] == "6":
        print(1 if isEmpty() else 0)
    if oper[0] == "7":
        print(mem[front + 1] if not isEmpty() else -1)
    if oper[0] == "8":
        print(mem[rear - 1] if not isEmpty() else -1)
