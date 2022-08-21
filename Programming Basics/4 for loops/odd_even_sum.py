number = int(input())
odd_numbers = 0
even_numbers = 0

for i in range(number):
    current_number = int(input())
    if i % 2 == 0:
        even_numbers += current_number
    else:
        odd_numbers += current_number

diff = abs(odd_numbers - even_numbers)

if even_numbers == odd_numbers:
    print("Yes")
    print(f"Sum = {even_numbers}")
else:
    print("No")
    print(f"Diff = {diff}")
