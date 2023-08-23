import sys

input = sys.stdin.readline

N = int(input())
todos = []
schedule = [[False] * 367 for _ in range(N)]  # 1~365까지 스케줄, 0과 366은 경계값
breakpoints = []
result = 0

for _ in range(N):
    S, E = map(int, input().split())
    todos.append((S, E))

todos.sort()

for todo in todos:
    S, E = todo
    for y in range(N):
        exist = False
        for x in range(S, E + 1):
            if schedule[y][x]:
                exist = True
                break
        if not exist:
            for x in range(S, E + 1):
                schedule[y][x] = True
            break


for x in range(367):  # breakpoints로 경계값 0, 366 포함
    exist = False
    for y in range(N):
        if schedule[y][x]:
            exist = True
            break
    if not exist:
        breakpoints.append(x)

for i in range(len(breakpoints) - 1):  # 마지막 하나는 제외
    if breakpoints[i] + 1 == breakpoints[i + 1]:  # 빈 일정이 연속된 경우
        continue
    leftmost, rightmost, topmost, bottommost = (
        breakpoints[i + 1] - 1,
        breakpoints[i] + 1,
        N - 1,
        0,
    )
    for y in range(0, N):
        for x in range(breakpoints[i] + 1, breakpoints[i + 1]):  # 스케줄 존재 구간
            if schedule[y][x]:
                leftmost = min(leftmost, x)
                rightmost = max(rightmost, x)
                topmost = min(topmost, y)
                bottommost = max(bottommost, y)

    result += (rightmost - leftmost + 1) * (bottommost - topmost + 1)

print(result)
