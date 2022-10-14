
number_of_invites = int(input())
invites = set()

for _ in range(number_of_invites):
    invited = input()
    invites.add(invited)

participants = set()

while True:
    actually_participated = input()
    if actually_participated == "END":
        break
    participants.add(actually_participated)

diff = invites - participants
print(len(diff))

print("\n".join(sorted(diff)))
