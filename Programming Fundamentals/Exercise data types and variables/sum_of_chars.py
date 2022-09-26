number_of_characters = int(input())

ascii_sum = 0

for i in range(number_of_characters):
    current_character = input()
    ascii_sum += ord(current_character)

print(f"The sum equals: {ascii_sum}")