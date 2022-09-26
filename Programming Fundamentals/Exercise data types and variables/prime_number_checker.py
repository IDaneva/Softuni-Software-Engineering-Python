number = int(input())

prime = True

if number > 1:
    for i in range (2, number):
        if number % i == 0:
            prime = False
if prime:
    print("True")
else:
    print("False")