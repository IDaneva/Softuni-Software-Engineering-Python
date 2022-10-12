number_of_pairs = int(input())
synonym_dict = {}

for _ in range(number_of_pairs):
    first_word, second_word = input(), input()
    if first_word not in synonym_dict:
        synonym_dict[first_word] = [second_word]
    else:
        synonym_dict[first_word].append(second_word)

print(synonym_dict)
for key, value in synonym_dict.items():
    print(f"{key} - {', '.join(value)}")

