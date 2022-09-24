n = int(input())
number = str(n)
condition = True

for a in range(1, 2):
    for b in range(4, 5):
        for c in range(1, 2):
            for d in range(3):
                if (a + b + c + d) == (a * b * c * d) and int(number[-1]) == 5:
                    print(f"{a}{b}{c}{d}")
                    condition = True
                    exit()

                elif (a * b * c * d) // (a + b + c + d) == 3 and n % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    condition = True
                    exit()
                else:
                    condition = False

if not condition:
    print("Nothing found")