from typing import List
from project_songs.album import Album

from project_songs.song import Song


class Band:

    def __init__(self, name):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        try:
            album1 = next(filter(lambda u: u.name == album_name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."

        if album1.published:
            return f"Album has been published. It cannot be removed."

        self.albums.remove(album1)
        return f"Album {album_name} has been removed."

    def details(self):
        result = [f"Band {self.name}"]
        [result.append(f"{s.details()}") for s in self.albums]
        return '\n'.join(result)
        # album_info = '\n'.join(Album.details(x) for x in self.albums)
        # return f'Band {self.name}\n' \
        #        f'{album_info}'


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())