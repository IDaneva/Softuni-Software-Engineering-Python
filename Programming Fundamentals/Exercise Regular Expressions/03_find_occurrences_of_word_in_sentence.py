import re

text = input()
searched_word = input()

search_pattern = fr"\b{searched_word}\b"
result = re.findall(search_pattern, text, flags=re.IGNORECASE)
print(len(result))
