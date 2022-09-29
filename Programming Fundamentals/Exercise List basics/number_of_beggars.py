string_money = input().split(", ")
number_of_beggars = int(input())

list_of_money = []
for i in string_money:
    list_of_money.append(int(i))

counter = 0
total_money = []
while counter < number_of_beggars:
    current_money = 0
    for money in list_of_money[counter::number_of_beggars]:
        current_money += money
    total_money.append(current_money)
    counter += 1
print(total_money)