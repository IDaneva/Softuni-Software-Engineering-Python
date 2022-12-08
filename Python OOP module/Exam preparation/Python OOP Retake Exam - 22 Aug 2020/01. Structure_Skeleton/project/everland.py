from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        expenses = [x.expenses + x.room_cost for x in self.rooms]
        return f"Monthly consumption: {sum(expenses):.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            if room.budget >= room.expenses + room.room_cost:
                room.budget -= room.expenses + room.room_cost
                result.append(f"{room.family_name} paid {(room.expenses + room.room_cost):.2f}$ and have {room.budget:.2f}$ left.")
                continue
            result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
            self.rooms.remove(room)
        return "\n".join(result)

    def status(self):
        all_people = [x.members_count for x in self.rooms]
        result = [f"Total population: {sum(all_people)}"]
        for room in self.rooms:
            result.append(str(room))
            if room.children:
                for child in room.children:
                    result.append(f"--- Child {room.children.index(child) + 1} monthly cost: {child.get_monthly_expense():.2f}$")
            result.append(f"--- Appliances monthly cost: {room.expenses:.2f}$")

        return "\n".join(result)
