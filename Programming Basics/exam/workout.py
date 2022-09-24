import math

number_of_days = int(input())
kilometers_she_ran_first_day = float(input())

additional_kilometers = 0
condition = True
total_km = 0



kilometers_per_day = 0
for days in range(number_of_days):
    percent_to_add_up = int(input()) / 100

    if days == 0:
        kilometers_per_day = kilometers_she_ran_first_day + percent_to_add_up * kilometers_she_ran_first_day
        total_km += kilometers_per_day
    else:
        kilometers_per_day = kilometers_per_day + (kilometers_per_day * percent_to_add_up)
        total_km += kilometers_per_day

overall = total_km + kilometers_she_ran_first_day
diff = abs(1000 - overall)

if overall >= 1000:
    print(f"You've done a great job running {math.ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(diff)} more kilometers")






