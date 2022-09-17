
saved_money = 0
condition = False

while True:
    destination = input("Destination? ")
    if destination == "End":
        break
    while destination != "End":
        needed_budget = float(input("Budget "))
        # if destination == "End":
        #     break
        while needed_budget > saved_money:
            saved_money += float(input("Saved Money "))
            if saved_money >= needed_budget:
                condition = True
                print(f'Going to {destination}!')
                break
        if condition:
            saved_money = 0
            break


