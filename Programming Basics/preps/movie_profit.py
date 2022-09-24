name_of_movie = input()
number_of_days = int(input())
number_of_tickets = int(input())
price_per_ticket = float(input())
percent_for_cinema_theatre = int(input()) / 100

total_profit_from_tickets = number_of_tickets * price_per_ticket
profit_for_the_whole_period = number_of_days * total_profit_from_tickets

for_cinema_theatre = percent_for_cinema_theatre * profit_for_the_whole_period

overall = profit_for_the_whole_period - for_cinema_theatre

print(f"The profit from the movie {name_of_movie} is {overall:.2f} lv.")