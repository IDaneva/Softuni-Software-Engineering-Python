movie = input()
package_type = input()
number_of_tickets = int(input())


if movie == "John Wick":
    if package_type == "Drink":
        price = 12
    elif package_type == "Popcorn":
        price = 15
    elif package_type == "Menu":
        price = 19
    total = number_of_tickets * price

elif movie == "Star Wars":
    if package_type == "Drink":
        price = 18
    elif package_type == "Popcorn":
        price = 25
    elif package_type == "Menu":
        price = 30
    total = number_of_tickets * price
    if number_of_tickets >= 4:
        total -= total * 0.3

elif movie == "Jumanji":
    if package_type == "Drink":
        price = 9
    elif package_type == "Popcorn":
        price = 11
    elif package_type == "Menu":
        price = 14
    total = number_of_tickets * price

    if number_of_tickets == 2:
        total -= total * 0.15


print(f"Your bill is {total:.2f} leva.")
