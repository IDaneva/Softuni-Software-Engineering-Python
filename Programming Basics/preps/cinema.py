theatre_capacity = int(input())

condition = False
total_income = 0

while True:
    number_of_people_entering = input()

    if number_of_people_entering == "Movie time!":
        condition = True
        break
    else:
        number_of_people = int(number_of_people_entering)

        tickets_profit = number_of_people * 5

        if number_of_people % 3 == 0:
            tickets_profit -= 5

        if number_of_people > theatre_capacity:
            print("The cinema is full.")
            break

        theatre_capacity -= number_of_people
        total_income += tickets_profit

if condition:
    print(f"There are {theatre_capacity} seats left in the cinema.")
print(f"Cinema income - {int(total_income)} lv.")


