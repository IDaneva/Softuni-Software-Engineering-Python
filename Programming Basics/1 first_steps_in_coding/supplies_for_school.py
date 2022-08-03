number_of_packets_pens = int(input())
number_of_packets_markers = int(input())
litres_cleaning_supplies = int(input())
discount_in_percentage = int(input())
packet_of_pens = 5.80
packet_of_markers = 7.20
cleaning_supplies_per_litre = 1.20
total_sum = number_of_packets_pens * packet_of_pens + number_of_packets_markers * packet_of_markers + litres_cleaning_supplies * cleaning_supplies_per_litre
total_sum_with_discount = total_sum - (total_sum * (discount_in_percentage / 100))
print(total_sum_with_discount)
