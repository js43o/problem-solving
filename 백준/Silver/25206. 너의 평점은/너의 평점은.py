import sys

input = sys.stdin.readline

totalCredit = 0
totalGrade = 0


def getGradeNumber(grade):
    SCORE = {"A": 4, "B": 3, "C": 2, "D": 1}
    if grade == "F":
        return 0
    return SCORE[grade[0]] + (0.5 if grade[1] == "+" else 0)


for i in range(20):
    title, credit, grade = input().rstrip().split()
    if grade == "P":
        continue
    totalCredit += float(credit)
    totalGrade += float(credit) * getGradeNumber(grade)

print(totalGrade / totalCredit)
