ammount = int(float(input()) * 100)
coins = 0

while ammount > 0:
    if ammount >= 200:
        ammount -= 200

    elif ammount >= 100:
        ammount -= 100

    elif ammount >= 50:
        ammount -= 50

    elif ammount >= 20:
        ammount -= 20

    elif ammount >= 10:
        ammount -= 10

    elif ammount >= 5:
        ammount -= 5

    elif ammount >= 2:
        ammount -= 2

    elif ammount >= 1:
        ammount -= 1

    coins += 1

print(coins)