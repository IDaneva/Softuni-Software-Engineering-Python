budget = int(input())
spent_money = 0

while True:
    price_of_product = input()

    if price_of_product == "End":
        print("You bought everything needed.")
        break
    elif price_of_product != "End":
        price_of_product = int(price_of_product)
        spent_money += price_of_product
        if spent_money > budget:
            print("You went in overdraft!")
            break