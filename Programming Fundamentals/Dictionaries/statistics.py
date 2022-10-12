my_dict = {}

while True:
    command = input()
    if command == "statistics":
        break
    data = command.split(": ")
    key = data[0]
    value = int(data[1])

    if key not in my_dict:
        my_dict[key] = value
    else:
        my_dict[key] += value

print(f"Products in stock:")

for keys in my_dict:
    values = my_dict[keys]
    print(f"- {keys}: {values}")

print(f"Total Products: {len(my_dict)}")
print(f"Total Quantity: {sum(my_dict.values())}")
