data = input().split()
dict_data = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}

print(dict_data)