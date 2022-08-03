annual_price_for_training = int(input())

sneakers = annual_price_for_training - (annual_price_for_training * 0.4)
kit = sneakers - (sneakers * 0.2)
ball = 0.25 * kit
accessories = 0.2 * ball

total_of_everything = annual_price_for_training + sneakers + kit + ball + accessories

print(total_of_everything)