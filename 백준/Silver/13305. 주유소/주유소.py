N = int(input())
roads = list(map(int, input().split()))
pays = list(map(int, input().split()))

pay = pays[0]
result = pays[0] * roads[0]
idx = 1

while idx < N - 1:
    if pays[idx] < pay:
        pay = pays[idx]
    result += pay * roads[idx]
    idx += 1

print(result)