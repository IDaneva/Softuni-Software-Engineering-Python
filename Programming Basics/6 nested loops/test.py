
command = ""
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

current_movie = ""

while command != "Finish":
    name_of_movie = input()
    available_seats = int(input())
    taken_seats = 0

    while True:
        bought_ticket = input()
        current_movie = name_of_movie

        if bought_ticket == "student":
            student_tickets += 1
        elif bought_ticket == "standard":
            standard_tickets += 1
        elif bought_ticket == "kid":
            kid_tickets += 1
        elif bought_ticket == "End":
            print(f"{current_movie} - {(taken_seats / available_seats * 100):.2f}% full.")
            break
        elif bought_ticket == "Finish":
            command = "Finish"
            print(f"{current_movie} - {(taken_seats/ available_seats * 100):.2f}% full.")
            break
        elif taken_seats >= available_seats:
            print(f"{current_movie} - {(taken_seats / available_seats * 100):.2f}% full.")
            break

        total_tickets += 1
        taken_seats += 1

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets * 100):.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets * 100):.2f}% standard tickets.")
print(f"{(kid_tickets / total_tickets * 100):.2f}% kids tickets.")
