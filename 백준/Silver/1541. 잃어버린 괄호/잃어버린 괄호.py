import re

str = input()

numbers = []
opers = []
temp = ""
idx = 0

# 문자열 파싱
while idx < len(str):
    if str[idx] == "+" or str[idx] == "-":
        numbers.append(int(temp))
        opers.append(str[idx])
        temp = ""
    else:
        temp += str[idx]
    idx += 1
numbers.append(int(temp))

result = numbers[0]
isSubtract = False

for i in range(0, len(opers)):
    if opers[i] == "-":
        isSubtract = True

    if isSubtract:
        result -= numbers[i + 1]
    else:
        result += numbers[i + 1]

print(result)
