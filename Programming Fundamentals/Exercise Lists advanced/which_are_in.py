first_string = input().split(", ")
second_string = input().split(", ")

sequence = []

for first_word in first_string:
    for second_word in second_string:
        if first_word in second_word and first_word not in sequence:
            sequence.append(first_word)
            break

print(sequence)