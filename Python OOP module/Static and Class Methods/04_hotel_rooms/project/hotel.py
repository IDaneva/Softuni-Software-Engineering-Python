from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            pass

        if not room.take_room(people):
            self.guests += people

    def free_room(self, room_number: int):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            pass

        if not room.free_room():
            self.guests -= room.guests

    def status(self):
        result = [f"Hotel {self.name} has {self.guests} total guests"]
        free_rooms = filter(lambda r: r.is_taken == False, self.rooms)
        list_of_free_rooms = [str(r.number) for r in free_rooms]
        taken_rooms = filter(lambda r: r.is_taken == True, self.rooms)
        list_of_taken_rooms = [str(r.number) for r in taken_rooms]
        result.append(f"Free rooms: {', '.join(list_of_free_rooms)}")
        result.append(f"Taken rooms: {', '.join(list_of_taken_rooms)}")
        return "\n".join(result)


hotel = Hotel.from_stars(5)

first_room = Room(1, 3)

second_room = Room(2, 2)

third_room = Room(3, 1)

hotel.add_room(first_room)

hotel.add_room(second_room)

hotel.add_room(third_room)

hotel.take_room(1, 4)

hotel.take_room(1, 2)

hotel.take_room(3, 1)

hotel.take_room(3, 1)

print(hotel.status())
