from math import ceil


class PhotoAlbum:
    PHOTOS_ON_A_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for x in range(pages)]    # create matrix of pages

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_ON_A_PAGE))

    def add_photo(self, label: str):
        for page in range(self.pages):
            if len(self.photos[page]) < self.PHOTOS_ON_A_PAGE:
                self.photos[page].append(label)

                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"

        return f"No more free slots"

    def display(self) -> str:
        result = ["-" * 11]

        for page in self.photos:  # photos is current page with 4 elements
            result.append(("[] " * len(page)).rstrip())
            result.append("-" * 11)

        return "\n".join(result)


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
