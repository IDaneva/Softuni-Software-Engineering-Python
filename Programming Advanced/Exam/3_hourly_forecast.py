def forecast(*args):
    # args will be tuples - location and current weather (Sofia, sunny)
    forecast_dict = {"Sunny": [], "Cloudy": [], "Rainy": []}
    for location_info in args:
        destination, weather = location_info
        forecast_dict[weather].append(destination)
        
    result = ""

    for key, value in forecast_dict.items():
        value = sorted(value)
        for city in value:
            result += f"{city} - {key}\n"

    return result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
