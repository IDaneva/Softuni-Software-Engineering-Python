chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
veggie_menu_price = 8.15
delivery = 2.50
dessert = 0.2

chicken_menu_total = chicken_menu_price * chicken_menu
fish_menu_total = fish_menu * fish_menu_price
veggie_menu_total = veggie_menu * veggie_menu_price
menus_total = chicken_menu_total + fish_menu_total + veggie_menu_total
dessert_total = dessert * menus_total

total_for_everything = menus_total + dessert_total + delivery

print(round(total_for_everything, 2))
