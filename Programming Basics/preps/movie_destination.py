movie_budget = float(input())
destination = input()
season = input()
number_of_days = float(input())
price = 0


if destination == "Dubai":
    if season == "Winter":
        price = 45000
    elif season == "Summer":
        price = 40000

    total_price_for_movie = number_of_days * price
    total_price_for_movie -= 0.3 * total_price_for_movie

elif destination == "Sofia":
    if season == "Winter":
        price = 17000
    elif season == "Summer":
        price = 12500

    total_price_for_movie = number_of_days * price
    total_price_for_movie += 0.25 * total_price_for_movie

elif destination == "London":
    if season == "Winter":
        price = 24000
    elif season == "Summer":
        price = 20250
    total_price_for_movie = number_of_days * price

diff = abs(movie_budget-total_price_for_movie)
if movie_budget >= total_price_for_movie:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")