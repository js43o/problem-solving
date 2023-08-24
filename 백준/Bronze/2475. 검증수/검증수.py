from functools import reduce

input = input()
numbers = input.split(' ')
result = 0
for i in numbers:
    result += (int(i) ** 2)

print(result % 10)
