import sys

input = sys.stdin.readline
MAX = 10**6

N = int(input())
cards = list(map(int, input().split()))
cards_default = cards.copy()
score = [0] * (MAX + 1)
index = [0] * (MAX + 1)
s = set(cards)

for i in range(N):
    index[cards[i]] = i  # 정렬 전 인덱스로 저장
cards.sort()

for card in cards:
    for i in range(2, MAX // card + 1):
        score[card * i] -= 1  # 배수에 해당되는 상대 플레이어 점수 -1
        if (card * i) in s:  # 배수가 실제로 다른 플레이어한테 있다면
            score[card] += 1  # 내 점수 +1

for card in cards_default:
    print(score[card], end=" ")
