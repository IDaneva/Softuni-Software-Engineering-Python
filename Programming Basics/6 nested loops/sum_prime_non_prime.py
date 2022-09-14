sum_of_prime_numbers = 0
sum_of_non_prime_numbers = 0

condition = False

while True:
    number = input()
    if number == "stop":
        break
    else:
        int_number = int(number)
        if int_number < 0:
            print("Number is negative.")
        else:
            if int_number >= 1:
                for deltitel in range(2, int_number):
                    if int_number % deltitel == 0:
                        condition = True
                        break
                    else:
                        condition = False
            if condition:
                sum_of_non_prime_numbers += int_number
            else:
                sum_of_prime_numbers += int_number

print(f"Sum of all prime numbers is: {sum_of_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_of_non_prime_numbers}")