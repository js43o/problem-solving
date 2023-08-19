import sys

input = sys.stdin.readline

units = [500, 100, 50, 10, 5, 1]
money = 1000 - int(input())
result = 0

for unit in units:
    if unit > money:
        continue
    result += money // unit
    money %= unit

print(result)
