import sys

input = sys.stdin.readline
gear = []
ptr = []  # 각 바퀴별 [왼쪽 톱니 인덱스, 오른쪽 톱니 인덱스] 배열
res = 0


def rotateGear(gearIndex, direction):
    ptr[gearIndex][0] = (ptr[gearIndex][0] - direction) % 8
    ptr[gearIndex][1] = (ptr[gearIndex][1] - direction) % 8


for _ in range(4):
    s = input().rstrip()
    gear.append(s)
    ptr.append([6, 2])

K = int(input())
for _ in range(K):
    n, d = map(int, input().split())
    n -= 1  # 0번부터 세기
    rotating = [0, 0, 0, 0]  # 기어별 회전할 방향
    rotating[n] = d

    for i in range(1, 4):  # 중앙부터 양끝으로 퍼져나가는 식으로 순회
        if n - i >= 0:  # 왼쪽 기어
            # 자신의 오른쪽 톱니가 자기 바로 오른쪽 기어의 왼쪽 톱니와 극이 다르다면
            if gear[n - i][ptr[n - i][1]] != gear[n - i + 1][ptr[n - i + 1][0]]:
                rotating[n - i] = -rotating[n - i + 1]  # 오른쪽 기어의 회전 방향과 반대로 회전
        if n + i < 4:  # 오른쪽 기어
            # 자신의 왼쪽 톱니가 자기 바로 왼쪽 기어의 오른쪽 톱니와 극이 다르다면
            if gear[n + i][ptr[n + i][0]] != gear[n + i - 1][ptr[n + i - 1][1]]:
                rotating[n + i] = -rotating[n + i - 1]  # 왼쪽 기어의 회전 방향과 반대로 회전

    for i in range(4):
        rotateGear(i, rotating[i])  # 각각 회전

for i in range(4):
    if gear[i][(ptr[i][0] + 2) % 8] == "1":  # 12시 톱니 == (왼쪽 톱니 + 2) % 8
        res += 2**i

print(res)
