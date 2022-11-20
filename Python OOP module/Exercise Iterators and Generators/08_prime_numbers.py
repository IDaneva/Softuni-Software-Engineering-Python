def get_primes(integers):
    for num in integers:
        if num <= 0 or num == 1:
            continue

        for n in range(2, num):
            if num % n == 0:
                break
        else:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
