str1 = input()
str2 = input()
arr = [0] * len(str2)

for i in range(len(str1)):
    temp = 0
    for j in range(len(str2)):
        if temp < arr[j]:
            temp = arr[j]
        elif str1[i] == str2[j]:
            arr[j] = temp + 1

print(max(arr))
