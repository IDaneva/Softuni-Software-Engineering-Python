pages_in_the_book = int(input())
per_hour = int(input())
days_for_the_book = int(input())
total_time_for_the_book = pages_in_the_book / per_hour
hour_per_day = total_time_for_the_book / days_for_the_book
print(round(hour_per_day))
