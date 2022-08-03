deposit_amount = float(input())
months = int(input())
anual_rate = float(input())

per_year = deposit_amount * ( anual_rate/100)
per_month = per_year / 12

total_amount = deposit_amount + months * per_month
print(total_amount)

