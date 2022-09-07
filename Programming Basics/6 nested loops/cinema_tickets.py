student_tickets = 0
standard_tickets = 0
kid_tickets = 0

total_tickets_sold = 0
current_movie_name = ""

command = False

while command != True:
    name_of_movie = input()

    if name_of_movie == "Finish":
        break
    else:
        available_seats = int(input())
        taken_seats = 0

        while True:
            type_of_ticket = input()

            if type_of_ticket == "End" or taken_seats >= available_seats:
                how_full_is_the_theatre = taken_seats / available_seats * 100
                current_movie_name = name_of_movie
                print(f"{current_movie_name} - {how_full_is_the_theatre:.2f}% full.")
                break
            else:
                if type_of_ticket == "student":
                    student_tickets += 1
                elif type_of_ticket == "standard":
                    standard_tickets += 1
                elif type_of_ticket == "kid":
                    kid_tickets += 1
                elif type_of_ticket == "Finish":
                    command = True
                    break

            taken_seats += 1
            total_tickets_sold += 1

print(f"Total tickets: {total_tickets_sold}")
print(f"{(student_tickets / total_tickets_sold * 100):.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets_sold * 100):.2f}% standard tickets.")
print(f"{(kid_tickets / total_tickets_sold * 100):.2f}% kids tickets.")