balance = 0

while True:
    amount = input()

    if amount == "NoMoreMoney":
        break

    amount = float(amount)

    if amount < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {amount:.2f}")
    balance += amount

print(f"Total: {float(balance):.2f}")
