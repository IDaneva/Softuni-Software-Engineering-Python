number_of_lines = int(input())
counter = 0

for _ in range(number_of_lines):
    symbol = input()
    if "(" in symbol:
        counter += 1
    elif ")" in symbol:
        counter -= 1
if 0 != counter:
    print("UNBALANCED")
else:
    print("BALANCED")