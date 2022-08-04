hour = int(input())
day = input()

if hour >= 10 and hour <= 18 and day in "Monday Tuesday Wednesday Thursday Friday Saturday":
    print("open")
else:
    print("closed")
