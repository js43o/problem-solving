import sys

input = sys.stdin.readline

N, B = map(int, input().split())
result = []
offset = ord("A") - 10

while N:
    val = str(N % B) if 0 <= N % B <= 9 else chr((N % B) + offset)
    result.append(val)
    N //= B

print("".join(list(reversed(result))))
