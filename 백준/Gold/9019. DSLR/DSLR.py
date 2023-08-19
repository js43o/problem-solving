from audioop import reverse
import sys
from collections import deque

input = sys.stdin.readline
S = ["_", "L", "R", "D", "S"]

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [(0, 0)] * 10000

    def get_form(num):
        if num <= 0:
            return [0, 0]

        l = (num - ((num // 1000) * 1000)) * 10 + (num // 1000)
        r = (num - ((num // 10) * 10)) * 1000 + (num // 10)

        return (l, r)

    def bfs():
        q = deque([A])
        visited[A] = (0, -1)

        while q:
            a = q.popleft()
            a_l, a_r = get_form(a)

            if a == B:
                return visited[a]

            if not visited[a_l][1]:
                q.append(a_l)
                visited[a_l] = (a, 1)  # 1 == L
                if a_l == B:
                    return visited[a_l]

            if not visited[a_r][1]:
                q.append(a_r)
                visited[a_r] = (a, 2)  # 2 == R
                if a_r == B:
                    return visited[a_r]

            if not visited[(a * 2) % 10000][1]:
                q.append((a * 2) % 10000)
                visited[(a * 2) % 10000] = (a, 3)  # 3 == D

            if not visited[(a - 1) % 10000][1]:
                q.append((a - 1) % 10000)
                visited[(a - 1) % 10000] = (a, 4)  # 4 == S

    last = bfs()
    result = ""
    while True:
        i, s = last[0], last[1]
        if s == -1:  # first component
            break
        result += S[s]
        last = visited[i]

    print(result[::-1])
