number_of_letters = int(input())

for ch1 in range(97, 97 + number_of_letters):
    for ch2 in range(97, 97 + number_of_letters):
        for ch3 in range(97, 97 + number_of_letters):
            print(f"{chr(ch1)}{chr(ch2)}{chr(ch3)}")

