import re

dates = input()

search_pattern = r"\b([0-3][0-9])(.|-|\/)([A-Z][a-z]{2})\2(\d{4})"

result = re.findall(search_pattern, dates)

for match in result:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
