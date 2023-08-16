N, k = map(int, input().split())
arr = list(map(int, input().split()))
winner = list(reversed(sorted(arr)))[:k]

print(winner[-1])
