from typing import List

from project_pizza.project import Band
from project_pizza.project import Drummer
from project_pizza.project import Guitarist
from project_pizza.project import Musician
from project_pizza.project import Singer
from project_pizza.project import Concert


class ConcertTrackerApp:

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []
        
    @property
    def musician_names(self):
        return [m.name for m in self.musicians]

    @property
    def band_names(self):
        return [b.name for b in self.bands]

    def _create_musician(self, musician_type: str, name: str, age: int):
        if musician_type == 'Guitarist':
            m = Guitarist(name, age)
        elif musician_type == 'Drummer':
            m = Drummer(name, age)
        else:
            m = Singer(name, age)
        return m

    def check_existing_musician_name_or_raise(self, name):
        if name in self.musician_names:
            raise Exception(f"{name} is already a musician!")

    def check_existing_band_name_or_raise(self, name):
        if name in self.band_names:
            raise Exception(f"{name} band is already created!")

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ("Guitarist", "Drummer", "Singer"):
            raise ValueError("Invalid musician type!")

        self.check_existing_musician_name_or_raise(name)
        m = self._create_musician(musician_type, name, age)
        self.musicians.append(m)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        self.check_existing_band_name_or_raise(name)
        b = Band(name)
        self.bands.append(b)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        existing_concerts = [x.place for x in self.concerts if x.place == place]
        if existing_concerts:
            raise Exception(f"{place} is already registered for {genre} concert!")

        c = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(c)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        if musician_name not in self.musician_names:
            raise Exception(f"{musician_name} isn't a musician!")

        if band_name not in self.band_names:
            raise Exception(f"{band_name} isn't a band!")

        existing_musician = [m for m in self.musicians if m.name == musician_name][0]
        existing_band = [b for b in self.bands if b.name == band_name][0]

        existing_band.members.append(existing_musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        if band_name not in self.band_names:
            raise Exception(f"{band_name} isn't a band!")
        existing_band = [b for b in self.bands if b.name == band_name][0]
        musicians = [x for x in existing_band.members if x.name == musician_name]

        if not musicians:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        musician = musicians[0]
        existing_band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]

        drummers = [x for x in band.members if isinstance(x, Drummer)]
        singers = [x for x in band.members if isinstance(x, Singer)]
        guitarists = [x for x in band.members if isinstance(x, Guitarist)]

        if not (singers and guitarists and drummers):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        are_singers_qualified = True
        for singer in singers:
            if concert.genre == 'Rock':
                if 'sing high pitch notes' not in singer.skills:
                    are_singers_qualified = False
            elif concert.genre == 'Metal':
                if 'sing low pitch notes' not in singer.skills:
                    are_singers_qualified = False
            else:
                if 'sing high pitch notes' not in singer.skills and 'sing low pitch notes' not in singer.skills:
                    are_singers_qualified = False

        are_drummer_qualified = True
        for drummer in drummers:
            if concert.genre == 'Rock':
                if 'play the drums with drumsticks' not in drummer.skills:
                    are_drummer_qualified = False
            elif concert.genre == 'Metal':
                if 'play the drums with drumsticks' not in drummer.skills:
                    are_drummer_qualified = False
            else:
                if 'play the drums with drum brushes' not in drummer.skills:
                    are_drummer_qualified = False

        are_guitarists_qualified = True
        for guitarist in guitarists:
            if concert.genre == 'Rock':
                if 'play rock' not in guitarist.skills:
                    are_guitarists_qualified = False
            elif concert.genre == 'Metal':
                if 'play metal' not in guitarist.skills:
                    are_guitarists_qualified = False
            else:
                if 'play jazz' not in guitarist.skills:
                    are_guitarists_qualified = False

        if not are_drummer_qualified or not are_guitarists_qualified or not are_singers_qualified:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
