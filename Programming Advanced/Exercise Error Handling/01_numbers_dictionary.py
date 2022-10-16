numbers_dictionary = {}
# loop so that the info for the dict can be filled
while True:
    try:
        command = input()
        if command == "Search":
            break
        number = int(input())
        numbers_dictionary[command] = number
    except ValueError:
        print("The variable number must be an integer")

# loop that searches for a value based on a given key
while True:
    number_as_string = input()
    if number_as_string == "Remove":
        break
    try:
        print(numbers_dictionary[number_as_string])
    except KeyError:
        print("Number does not exist in dictionary")

# loop that removes key-value pair based on given key
while True:
    to_be_removed_number = input()
    if to_be_removed_number == "End":
        break
    try:
        del numbers_dictionary[to_be_removed_number]
    except KeyError:
        print("Number does not exist in dictionary")

print(numbers_dictionary)
