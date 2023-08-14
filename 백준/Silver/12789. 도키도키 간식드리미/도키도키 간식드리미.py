import sys
from collections import deque

input = sys.stdin.readline


N = int(input())
students = deque(list(map(int, input().split())))
count = 0
stk = []

while students:
    student = students.popleft()
    if student == count + 1:
        count += 1
    else:
        stk.append(student)

    while stk:  # 스택 체크
        if stk[-1] == count + 1:
            stk.pop()
            count += 1
        else:
            break

if count == N and len(stk) == 0:
    print("Nice")
else:
    print("Sad")
