key = int(input())
number_of_lines = int(input())

current_word = ""
for _ in range(number_of_lines):
    letter = input()
    current_word += chr(ord(letter) + key)

print(current_word)