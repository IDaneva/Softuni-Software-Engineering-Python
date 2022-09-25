year = int(input())

condition = True
while condition:
    year += 1
    set_year = set()

    for i in range(len(str(year))):
        set_year.add(str(year)[i])

        if len(str(year)) == len(set_year):
            print(year)
            condition = False
            break


