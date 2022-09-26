number_of_snowballs = int(input())

best_snowball_value = 0
best_snowball_weight = 0
best_snowball_time = 0
best_snowball_quality = 0


for snowballs in range(number_of_snowballs):
    current_snowball_weight = int(input())
    current_snowball_time = int(input())
    current_snowball_quality = int(input())

    current_snowball_value = (current_snowball_weight/current_snowball_time) ** current_snowball_quality

    if current_snowball_value > best_snowball_value:
        best_snowball_value = current_snowball_value
        best_snowball_weight = current_snowball_weight
        best_snowball_time = current_snowball_time
        best_snowball_quality = current_snowball_quality
print(f"{best_snowball_weight} : {best_snowball_time} = {int(best_snowball_value)} ({best_snowball_quality})")

