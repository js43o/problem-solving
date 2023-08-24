import sys

queue = []
n = int(input())

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push_front":
        arg = command[1]
        queue.insert(0, arg)
    elif command[0] == "push_back":
        arg = command[1]
        queue.append(arg)
    elif command[0] == "pop_front":
        if len(queue) > 0:
            print(queue[0])
            queue.remove(queue[0])
        else:
            print(-1)
    elif command[0] == "pop_back":
        print(queue.pop() if len(queue) > 0 else -1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(1 if len(queue) == 0 else 0)
    elif command[0] == "front":
        print(queue[0] if len(queue) > 0 else -1)
    elif command[0] == "back":
        print(queue[len(queue) - 1] if len(queue) > 0 else -1)
