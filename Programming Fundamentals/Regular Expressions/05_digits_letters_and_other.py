def digit_finder(sequence):
    return "".join([str(ch) for ch in sequence if ch.isdigit()])


def letter_finder(sequence):
    return "".join([str(ch) for ch in sequence if ch.isalpha()])


def other_symbols_finder(sequence):
    return "".join([str(ch) for ch in sequence if not ch.isdigit() and not ch.isalpha()])


sequence_to_be_filtered = input()
print(digit_finder(sequence_to_be_filtered))
print(letter_finder(sequence_to_be_filtered))
print(other_symbols_finder(sequence_to_be_filtered))
