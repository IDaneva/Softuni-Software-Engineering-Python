movie_type = input()
rows = int(input())
columns = int(input())

seats = rows * columns
price = 0


if movie_type == "Premiere":
    price = 12.00
elif movie_type == "Normal":
    price = 7.50
elif movie_type == "Discount":
    price = 5.00

income = seats * price
print(f" {income:.2f} leva")

