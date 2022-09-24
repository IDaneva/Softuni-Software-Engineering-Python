city = input()
package_type = input()
vip_discount = input()
days = int(input())

price = 0

if city == "Bansko" or city == "Borovets":
    if package_type == "withEquipment":
        price = 100
        if vip_discount == "yes":
            price -= price * 0.1
    else:
        price = 80
        if vip_discount == "yes":
            price -= price * 0.05

elif city == "Varna" or city == "Burgas":
    if package_type == "withBreakfast":
        price = 130
        if vip_discount == "yes":
            price -= price * 0.12
    else:
        price = 100
        if vip_discount == "yes":
            price -= price * 0.07

if days < 1:
    print("Days must be positive number!")

elif city != "Varna" and city != "Burgas" and city != "Bansko" and city != "Borovets":
    print("Invalid input!")
else:
    if days >= 7:
        total = (days - 1) * price
        print(f"The price is {total:.2f}lv! Have a nice time!")
    else:
        total = days * price
        print(f"The price is {total:.2f}lv! Have a nice time!")


