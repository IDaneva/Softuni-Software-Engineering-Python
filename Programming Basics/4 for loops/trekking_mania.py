number_of_groups = int(input())

Musala = 0
Montblan = 0
Kalibanjaro = 0
K2 = 0
Everest = 0

for _ in range(number_of_groups):
    number_of_climbers = int(input())
    if number_of_climbers <= 5:
        Musala += number_of_climbers
    elif 6 <= number_of_climbers <= 12:
        Montblan += number_of_climbers
    elif 13 <= number_of_climbers <= 25:
        Kalibanjaro += number_of_climbers
    elif 26 <= number_of_climbers <= 40:
        K2 += number_of_climbers
    elif 41 <= number_of_climbers:
        Everest += number_of_climbers

total = Musala + Montblan + Kalibanjaro + K2 + Everest

print(f"{Musala/total * 100:.2f}%")
print(f"{Montblan/total * 100:.2f}%")
print(f"{Kalibanjaro/total * 100:.2f}%")
print(f"{K2/total * 100:.2f}%")
print(f"{Everest/total * 100:.2f}%")


