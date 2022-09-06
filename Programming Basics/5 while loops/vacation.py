trip_price = float(input())
available_money = float(input())

days = 0
spending_days = 0

while trip_price > available_money:
    command = input()
    ammount = float(input())

    if command == "spend":
        spending_days += 1
        if spending_days == 5:
            print("You can't save the money.")
            days += 1
            print(f"{days}")
            break
        else:
            available_money -= ammount
            if available_money < 0:
                available_money = 0

    if command == "save":
        available_money += ammount
        spending_days = 0

    days += 1

if available_money >= trip_price:
    print(f"You saved the money for {days} days.")