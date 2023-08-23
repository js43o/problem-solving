import calendar
a = input()
b = a.split()
c = calendar.weekday(2007, int(b[0]), int(b[1]))
if c == 0:
    print("MON")
elif c == 1:
    print("TUE")
elif c == 2:
    print("WED")
elif c == 3:
    print("THU")
elif c == 4:
    print("FRI")
elif c == 5:
    print("SAT")
elif c == 6:
    print("SUN")