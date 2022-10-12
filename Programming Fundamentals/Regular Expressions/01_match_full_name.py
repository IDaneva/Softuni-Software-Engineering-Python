import re

names = input()

search_pattern = r"\b([A-Z][a-z]+) ([A-Z][a-z]+)\b"

result = re.findall(search_pattern, names)

for match in result:
    print(" ".join(match), end=" ")
