import re

phones = input()

search_pattern = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"

matches = re.findall(search_pattern, phones)

print(", ".join(matches))
