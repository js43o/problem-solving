import sys

input = sys.stdin.readline

N, B = input().rstrip().split()
offset = 10 - ord("A")
result = 0

for i in range(len(N)):
    char = N[len(N) - 1 - i]
    val = int(char) if "0" <= char <= "9" else ord(char) + offset
    result += val * (int(B) ** i)

print(result)
