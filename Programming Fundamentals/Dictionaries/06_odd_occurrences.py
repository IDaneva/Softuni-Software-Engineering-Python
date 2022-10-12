words = input().split()

word_dict = {}
for current_word in words:
    if current_word.lower() not in word_dict:
        word_dict[current_word.lower()] = 1
        continue
    word_dict[current_word.lower()] += 1

print(word_dict)
odd_occurrences = [key for key, values in word_dict.items() if values % 2 != 0]
print(" ".join(odd_occurrences))
