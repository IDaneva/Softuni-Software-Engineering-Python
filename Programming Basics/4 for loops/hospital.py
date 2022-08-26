period = int(input())

docs = 7

treated = 0
untreated = 0

for days in range(1, period + 1):
    patients = int(input("Number of patients? "))
    if days % 3 == 0:
        if untreated > treated:
            docs += 1

    if patients <= docs:
        treated += patients

    elif patients > docs:
        untreated += patients - docs
        treated += docs



print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")
