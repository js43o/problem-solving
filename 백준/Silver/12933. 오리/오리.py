sound = input()

ducks = []
CORRECT_LENGTH = {"q": 0, "u": 1, "a": 2, "c": 3, "k": 4}

for c in sound:
    isExist = False
    for duck in ducks:
        if len(duck) == CORRECT_LENGTH[c]:  # 조건에 맞는 오리 찾기
            isExist = True
            if c == "k":  # 울음소리를 완성한 경우
                duck.clear()
            else:
                duck.append(c)
            break
    if not isExist:  # 적당한 오리를 찾지 못했을 때
        if c == "q":  # 새로운 오리가 나타나야 하는 경우
            ducks.append([c])
            continue
        print(-1)
        exit()

for duck in ducks:
    if len(duck) > 0:
        print(-1)
        exit()
print(len(ducks))
