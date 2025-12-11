class Book:
    """Книга с флагом статуса прочтения."""
    def __init__(self, title: str, author: str, year: int, is_read: bool = False):
        self.title = title
        self.author = author
        self.year = int(year)
        self.is_read = bool(is_read)

    def read_book(self) -> None:
        self.is_read = True
