from typing import Tuple, List
from project_songs.song import Song


class Album:

    def __init__(self, name: str, *songs: Song):     # receive one or more song names in tuple of strings
        self.name = name
        self.songs: List[Song] = list(songs)               # list(*(unpack)songs)
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return f"Cannot add songs. Album is published."

        if song in self.songs:
            return f"Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        try:
            song = next(filter(lambda y: y.name == song_name, self.songs))  # match song_name with objects in self.songs
        except StopIteration:
            return f"Song is not in the album."                             # if no match return message

        if self.published:
            return f"Cannot remove songs. Album is published."

        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        album_info = [f"Album {self.name}"]
        [album_info.append(f"== {x.get_info()}") for x in self.songs]
        return "\n".join(album_info)
