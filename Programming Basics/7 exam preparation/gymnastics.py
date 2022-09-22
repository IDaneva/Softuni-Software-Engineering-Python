country = input()
device = input()

total = 0

if country == "Russia":
    if device == "ribbon":
        first_evaluation = 9.1
        second_evaluation = 9.4
        total += first_evaluation + second_evaluation

    elif device == "hoop":
        first_evaluation = 9.3
        second_evaluation = 9.8
        total += first_evaluation + second_evaluation

    elif device == "rope":
        first_evaluation = 9.6
        second_evaluation = 9
        total += first_evaluation + second_evaluation

elif country == "Bulgaria":
    if device == "ribbon":
        first_evaluation = 9.6
        second_evaluation = 9.4
        total += first_evaluation + second_evaluation

    elif device == "hoop":
        first_evaluation = 9.55
        second_evaluation = 9.75
        total += first_evaluation + second_evaluation

    elif device == "rope":
        first_evaluation = 9.5
        second_evaluation = 9.4
        total += first_evaluation + second_evaluation

elif country == "Italy":
    if device == "ribbon":
        first_evaluation = 9.2
        second_evaluation = 9.5
        total += first_evaluation + second_evaluation

    elif device == "hoop":
        first_evaluation = 9.45
        second_evaluation = 9.35
        total += first_evaluation + second_evaluation

    elif device == "rope":
        first_evaluation = 9.7
        second_evaluation = 9.15
        total += first_evaluation + second_evaluation

diff = 20 - total
percentage = diff / 20 * 100

print(f"The team of {country} get {total:.3f} on {device}.")
print(f"{percentage:.2f}%")
