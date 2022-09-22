number_of_movies = int(input())

max_rating = 0
max_movie = ""

low_rating = 11
low_movie = ""

total = 0

for movie in range(number_of_movies):
    name_of_movie = input()
    rating = float(input())

    if rating >= max_rating:
        max_rating = rating
        max_movie = name_of_movie

    if rating < low_rating:
        low_rating = rating
        low_movie = name_of_movie

    total += rating

print(f"{max_movie} is with highest rating: {max_rating}")
print(f"{low_movie} is with lowest rating: {low_rating}")
print(f"Average rating: {(total / number_of_movies):.1f}")

