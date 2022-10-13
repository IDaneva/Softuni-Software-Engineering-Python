from collections import deque

people_at_the_cash_desk = deque()

while True:
    command = input()
    if command == "End":
        break
    else:
        if command == "Paid":
            print("\n".join(people_at_the_cash_desk))
            people_at_the_cash_desk.clear()

        else:
            name = command
            people_at_the_cash_desk.append(name)

print(f"{len(people_at_the_cash_desk)} people remaining.")
