air_line = input()
adults_tickets = int(input())
childrens_tickets = int(input())
net_price_for_adult = float(input())
net_price_for_child = net_price_for_adult - 0.7 * net_price_for_adult
obslujvane = float(input())

price_for_adult = net_price_for_adult + obslujvane
price_for_child = net_price_for_child + obslujvane

total_for_adult_tickets = adults_tickets * price_for_adult
total_for_childrens_tickets = childrens_tickets * price_for_child

profit = (total_for_adult_tickets + total_for_childrens_tickets) * 0.2

print(f"The profit of your agency from {air_line} tickets is {profit:.2f} lv.")