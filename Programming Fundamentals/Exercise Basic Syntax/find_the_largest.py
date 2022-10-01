
number = int(input())
digits = []
for i in range(len(str(number))):
    digits.append(int(str(number)[i]))

digits.sort(reverse=True)
for item in digits:
    print(item, end="")


