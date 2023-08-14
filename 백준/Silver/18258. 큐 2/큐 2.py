import sys

input = sys.stdin.readline


q = []
front = -1  # 항상 존재하는 맨앞의 원소를 가리킴
N = int(input())


def isEmpty():
    return front == -1 or len(q) == front


for _ in range(N):
    oper = input().rstrip().split()
    if oper[0] == "push":
        q.append(int(oper[1]))
        if front == -1:
            front += 1
    if oper[0] == "pop":
        if not isEmpty():
            print(q[front])
            front += 1
        else:
            print(-1)
    if oper[0] == "size":
        print(len(q) - front if not isEmpty() else 0)
    if oper[0] == "empty":
        print(1 if isEmpty() else 0)
    if oper[0] == "front":
        print(q[front] if not isEmpty() else -1)
    if oper[0] == "back":
        print(q[len(q) - 1] if not isEmpty() else -1)
