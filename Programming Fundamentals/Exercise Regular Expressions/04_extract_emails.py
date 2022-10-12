import re

searched_pattern = r"(?<=\s)([a-z]+[\-\.\_a-z]*@[a-z]+[\-\.\_a-z]+\.[a-z]+[\-\.\_a-z]*)\b"
text = input()
result = re.findall(searched_pattern, text)

for match in result:
    print(match)