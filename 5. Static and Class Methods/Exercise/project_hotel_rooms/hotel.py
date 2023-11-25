from typing import List
from project_hotel_rooms.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = [x for x in self.rooms if x.number == room_number][0]
        result = room.take_room(people)
        if result:
            return result
        self.guests += people

    def free_room(self, room_number: int):
        room = [x for x in self.rooms if x.number == room_number][0]
        if room:
            guests = room.guests
            result = room.free_room()
            if result:
                return result

            self.guests -= guests

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n"\
               f"Free rooms: {', '.join(str(x.number) for x in self.rooms if not x.is_taken)}\n"\
               f"Taken rooms: {', '.join(str(x.number) for x in self.rooms if x.is_taken)}"
