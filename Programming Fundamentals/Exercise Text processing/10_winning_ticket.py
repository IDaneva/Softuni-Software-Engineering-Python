# def ticket_validator(ticket):
#     if len(ticket) == 20:
#         return True
#     else:
#         return f"invalid ticket"
#
#
# def winner_finder(ticket):
#     left_side = ticket[:10]
#     right_side = ticket[10:]
#     winning_symbols = ['@', '#', '$', '^']
#     for current_symbol in winning_symbols:
#         for win_combinations in range(10, 5, -1):
#             if current_symbol * win_combinations in left_side and current_symbol * win_combinations in right_side:
#                 if win_combinations == 10:
#                     print(f"ticket \"{ticket}\" - {win_combinations}{current_symbol} Jackpot!")
#                     break
#                 else:
#                     print(f"ticket \"{ticket}\" - {win_combinations}{current_symbol}")
#                     break
#             else:
#                 continue
#
#
# collection_of_tickets = input().split(", ")
#
# for current_ticket in collection_of_tickets:
#     if ticket_validator(current_ticket) and winner_finder(current_ticket):
#         winner_finder(current_ticket)
#         continue
#     elif ticket_validator(current_ticket) and not winner_finder(current_ticket):
#         print(f"ticket '{current_ticket}' - no match")
#


collection_of_tickets = input().split(",")
new_collection_without_spaces = [s.strip() for s in collection_of_tickets]

for current_ticket in new_collection_without_spaces:
    if len(current_ticket) == 20:
        validated_length = True
    else:
        validated_length = False
        print(f"invalid ticket")
        continue

    if validated_length:
        left_side = current_ticket[:10]
        right_side = current_ticket[10:]
        winning_symbols = ['@', '#', '$', '^']
        found_winner = False
        for current_symbol in winning_symbols:
            if found_winner:
                break
            for win_combinations in range(10, 5, -1):
                if current_symbol * win_combinations in left_side and current_symbol * win_combinations in right_side:
                    if win_combinations == 10:
                        print(f"ticket \"{current_ticket}\" - {win_combinations}{current_symbol} Jackpot!")
                        found_winner = True
                        break
                    elif win_combinations != 10:
                        print(f"ticket \"{current_ticket}\" - {win_combinations}{current_symbol}")
                        found_winner = True
                        break
                    else:
                        found_winner = False
                        break
        if not found_winner:
            print(f"ticket \"{current_ticket}\" - no match")

