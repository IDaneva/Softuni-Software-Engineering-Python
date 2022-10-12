data = input().split()
dict_data = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}

products_to_search = input().split()
for current_product in products_to_search:
    if current_product in dict_data:
        print(f"We have {dict_data[current_product]} of {current_product} left")
        continue
    print(f"Sorry, we don't have {current_product}")