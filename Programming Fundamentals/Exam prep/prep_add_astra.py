import re

text_string = input()
search_pattern = r"(#|\|)([A-Za-z ]+)\1([0-9][0-9]\/[0-9][0-9]\/[0-9][0-9])\1(\d+)\1"
result = re.finditer(search_pattern, text_string)

total_calories = 0
for match in result:
    total_calories += int(match.group(4))

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
result2 = re.finditer(search_pattern, text_string)

for match2 in result2:
    print(f"Item: {match2.group(2)}, Best before: {match2.group(3)}, Nutrition: {match2.group(4)}")

