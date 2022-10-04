def palindrome(numbers):
    for x in numbers:
        if x == x[::-1]:
            print(True)
        else:
            print(False)


sequence_of_numbers = input().split(", ")
palindrome(sequence_of_numbers)
