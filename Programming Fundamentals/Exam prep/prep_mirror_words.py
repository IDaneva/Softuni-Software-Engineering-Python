import re

text_string = input()
search_pattern = r"(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"

result = re.finditer(search_pattern, text_string)
word_pairs = 0
mirror_words = []

for match in result:
    word_pairs += 1
    if match.group(2) == (match.group(3))[::-1]:
        mirror_words.append(f'{match.group(2)} <=> {match.group(3)}')

if word_pairs == 0 and len(mirror_words) == 0:
    print(f"No word pairs found!")
    print("No mirror words!")

else:
    print(f"{word_pairs} word pairs found!")
    if len(mirror_words) == 0:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(f"{', '.join(mirror_words)}")