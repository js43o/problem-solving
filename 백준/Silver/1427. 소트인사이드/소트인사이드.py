number = input()
result = []

max = 0
index = 0

for i in range(0, len(number)):
    for j in range(0, len(number)):
        if int(number[j]) > max:
            max = int(number[j])
            index = j
    result.append(str(max))
    number = number[0:index] + number[(index+1):]
    max = 0

print(''.join(result))
