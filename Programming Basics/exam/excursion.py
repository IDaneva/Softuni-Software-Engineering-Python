number_of_people_in_group = int(input())
number_of_nights = int(input())
number_of_transport_cards = int(input())
number_of_museum_tickets = int(input())

night = 20
transportation_card = 1.60
museum_entrance = 6

price_for_one_person_for_stay = number_of_nights * night
price_for_one_for_transport = transportation_card * number_of_transport_cards
price_for_one_for_museum = museum_entrance * number_of_museum_tickets

total_for_one = price_for_one_person_for_stay + price_for_one_for_transport + price_for_one_for_museum

total_for_group = total_for_one * number_of_people_in_group

totaal = total_for_group + (total_for_group * 0.25)

print(f"{totaal:.2f}")
