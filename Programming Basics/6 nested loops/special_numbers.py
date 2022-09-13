number = int(input())

for index1 in range(1, 10):
    for index2 in range(1, 10):
        for index3 in range(1, 10):
            for index4 in range(1, 10):
                if number % index1 == 0 and number % index2 == 0 and number % index3 == 0 and number % index4 == 0:
                    print(f"{index1}{index2}{index3}{index4}", end=" ")
