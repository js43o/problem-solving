import sys

input = sys.stdin.readline

N, H = map(int, input().split())
lower = [0] * (H + 1)  # 석순의 크기별 누적 개수 (아래에서 위로 누적)
upper = [0] * (H + 1)  # 종유석의 크기별 누적 개수 (위에서 아래로 누적)
obstacle = []  # 0 ~ H 구간의 장애물 누적 총합

for i in range(N):
    size = int(input())
    if i % 2 == 0:
        lower[size] += 1
    else:
        upper[size] += 1

for h in range(H - 2, 0, -1):  # 석순, 종유석 각각 높은 쪽부터 낮은 쪽으로 누적
    upper[h] += upper[h + 1]
    lower[h] += lower[h + 1]

for h in range(1, H + 1):  # h 구간의 장애물 총합 구하기
    obstacle.append(lower[h] + upper[H - h + 1])

min_val = min(obstacle)
print(min_val, obstacle.count(min_val), end=" ")
