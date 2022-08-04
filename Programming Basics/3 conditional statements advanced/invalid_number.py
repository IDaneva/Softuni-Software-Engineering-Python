number = int(input())
valid = True
if 100 <= number <= 200 or number == 0:
    valid = True
else:
    valid = False

if valid == False:
    print("invalid")
