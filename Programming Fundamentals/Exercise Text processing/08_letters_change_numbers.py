sequence_of_strings = input().split()
result = 0

alphabet = [chr(i) for i in range(65, 91)]

for current_sequence in sequence_of_strings:
    number_to_do_math = int(current_sequence[1:-1])

    if current_sequence[0].isupper():
        letter_position = int((alphabet.index(current_sequence[0].upper())) + 1)
        result += number_to_do_math / letter_position
    elif current_sequence[0].islower():
        letter_position = int((alphabet.index(current_sequence[0].upper())) + 1)
        result += number_to_do_math * letter_position

    if current_sequence[-1].isupper():
        letter_position = int((alphabet.index(current_sequence[-1].upper())) + 1)
        result -= letter_position
    elif current_sequence[-1].islower():
        letter_position = int((alphabet.index(current_sequence[-1].upper())) + 1)
        result += letter_position

print(f"{result:.2f}")