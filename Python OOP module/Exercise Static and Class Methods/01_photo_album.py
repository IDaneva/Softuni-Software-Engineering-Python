class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        needed_pages = photos_count // 4
        if photos_count % 4 != 0:
            needed_pages += 1

        return cls(needed_pages)

    def add_photo(self, label: str):
        for p in self.photos:
            if len(p) < 4:
                p.append(label)
                return f"{label} photo added successfully on page {self.photos.index(p)} slot {p.index(label)}"

        return "No more free slots"

    def display(self):
        result = ["-" * 11]
        for page in self.photos:
            result.append(('[] ' * len(page)).rstrip())
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
