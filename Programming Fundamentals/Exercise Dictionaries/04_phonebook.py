phone_dict = {}

while True:
    command = input()
    if "-" not in command:
        number_of_searches = int(command)
        break
    name, phone_number = command.split("-")
    phone_dict[name] = phone_number

for _ in range(number_of_searches):
    searched_person = input()
    if searched_person in phone_dict:
        print(f"{searched_person} -> {phone_dict[searched_person]}")
    else:
        print(f"Contact {searched_person} does not exist.")

