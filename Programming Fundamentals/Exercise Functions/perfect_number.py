def aliquot(num):
    sum = 0
    for current_num in range(1, num):
        if num % current_num == 0:
            sum += current_num
    if num == sum:
        return True


number = int(input())

if aliquot(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
