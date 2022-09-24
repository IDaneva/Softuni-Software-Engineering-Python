movie_counter = 0

max_points = 0
max_movie = ""

condition = False

while True:
    name_of_movie = input()
    total_points = 0

    if name_of_movie == "STOP":
        break

    movie_counter += 1

    if movie_counter == 7:
        condition = True
        break
    current_points = 0

    for ch in name_of_movie:
        points = ord(ch)


        if ch in "QWERTYUIOPASDFGHJKLZXCVBNM":
            points -= len(name_of_movie)

        elif ch in "qwertyuiopasdfghjklzxcvbnm":
            points -= 2 * len(name_of_movie)

        current_points += points

    total_points += current_points

    if total_points > max_points:
        max_points = total_points
        max_movie = name_of_movie

if condition:
    print("The limit is reached.")

print(f"The best movie for you is {max_movie} with {max_points} ASCII sum.")