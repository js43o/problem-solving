import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
palindrome = [[False] * N for _ in range(N)]

# 홀수 길이 팰린드롬 찾기
for mid in range(N):
    palindrome[mid][mid] = True  # 자기 자신은 길이 1의 팰린드롬

    for offset in range(1, N // 2 + 1):
        if mid - offset < 0 or mid + offset >= N:
            break
        if arr[mid - offset] != arr[mid + offset]:  # 중간에 팰린드롬이 끊기면 종료
            break
        palindrome[mid - offset][mid + offset] = True
        palindrome[mid + offset][mid - offset] = True

# 짝수 길이 팰린드롬 찾기
for mid in range(N - 1):
    if arr[mid] != arr[mid + 1]:
        continue
    palindrome[mid][mid + 1] = True
    palindrome[mid + 1][mid] = True

    for offset in range(1, N // 2 + 1):
        if mid - offset < 0 or (mid + 1) + offset >= N:
            break
        if arr[mid - offset] != arr[(mid + 1) + offset]:
            break
        palindrome[mid - offset][(mid + 1) + offset] = True
        palindrome[(mid + 1) + offset][mid - offset] = True


for _ in range(M):
    S, E = map(lambda x: int(x) - 1, input().split())
    print(1 if palindrome[S][E] else 0)
