countries, capitals = input().split(", "), input().split(", ")
country_dict = {countries[i]:capitals[i] for i in range(len(capitals))}
for key, value in country_dict.items():
    print(f"{key} -> {value}")

