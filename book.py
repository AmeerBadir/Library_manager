class Book:
    """
    A class that represent a Book, each book have his title,author,
     publication year and genre

    """

    def __init__(self, title, author, publication_year, genre):
        self._title = title
        self._author = author
        self._publication_year = publication_year
        self._genre = genre

    def get_author(self):
        return self._author

    def get_genre(self):
        return self._genre

    def is_same_book(self, other):
        if self._title == other.get_title() and self._author == other.get_author():
            if self._genre == other.get_genre():
                if self._publication_year == other.get_publication_year():
                    return True
        return False

    def set_title(self, new_title):
        self._title = new_title

    def get_publication_year(self):
        return self._publication_year

    def get_title(self):
        return self._title

    def set_author(self, new_author):
        self._author = new_author

    def set_genre(self, new_genre):
        self._genre = new_genre

    def set_publication_year(self, publication_year):
        self._publication_year = publication_year

    def display_book(self):
        return (f"title: {self._title}, author: {self._author}, publication year: {self._publication_year}, "
                f"gener: {self._genre} ")
