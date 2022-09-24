
expected_profit = float(input())
made_profit = 0

while True:
    command = input()

    if command == "Party!":
        print(f"We need {(abs(expected_profit- made_profit)):.2f} leva more.")
        break

    else:
        number_of_drinks = int(input())
        price_per_drink = len(command)
        order_price = number_of_drinks * price_per_drink
        if order_price % 2 != 0:
            order_price -= order_price * 0.25

        made_profit += order_price

        if made_profit >= expected_profit:
            print("Target acquired.")
            break

print(f"Club income - {(made_profit):.2f} leva.")