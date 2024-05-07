from book import Book


class Library:
    """
    A library class
    """

    def __init__(self):
        # list of book in the library
        self._books_list = []
        # a dictionary where is the key is the author and the value of the key is a
        # list of books of this author
        self._books_by_author = dict()
        # a dictionary where is the key is the genre and the value of the key is a list of books of the genre
        self._books_by_genre = dict()

    def add_book_to_library(self, book: Book):
        """
        Adding book to the library, and then update the author dictionary and the genre dictionary

        :param book:  book to add
        :return:
        """
        self._books_list.append(book)
        if book.get_genre() in self._books_by_genre:
            self._books_by_genre[book.get_genre()].append(book)
        else:
            self._books_by_genre[book.get_genre()] = [book]
        if book.get_author() in self._books_by_author:
            self._books_by_author[book.get_author()].append(book)
        else:
            self._books_by_author[book.get_author()] = [book]

    def delete_book(self, book_to_delete: Book):
        if self.remove_book_from_list(self._books_list, book_to_delete):
            genre = book_to_delete.get_genre()
            self.remove_book_from_list(self._books_by_genre[genre], book_to_delete)
            author = book_to_delete.get_author()
            self.remove_book_from_list(self._books_by_author[author], book_to_delete)
            print("Deleting book successfully")
        else:
            print("Deleting failed")

    def remove_book_from_list(self, book_list, book_to_delete: Book):
        book_in_list = False
        for book in book_list:
            if book_to_delete.is_same_book(book):
                book_list.remove(book)
                book_in_list = True
        return book_in_list

    def display_library_books(self):
        for book in self._books_list:
            print(book.display_book())

    def display_book_by_gener(self, genre):
        if genre not in self._books_by_genre:
            print(f"There is no book in genre {genre} in the library")
        else:
            for book in self._books_by_genre[genre]:
                print(book.display_book())

    def display_book_by_author(self, author):
        if author not in self._books_by_author:
            print(f"Author {author} not found")
        else:
            for book in self._books_by_author[author]:
                print(book.display_book())

    def write_library_file(self):
        try:
            f = open("demo_file2.txt", "w")
            for book in self._books_list:
                f.write(book.display_book() + "\n")
        except:
            print("An exception occurred in opening the file")

    def create_library_by_file(self, library_file):
        try:
            file1 = open(library_file, 'r')
            lines = file1.readlines()
            for line in lines:
                book_attributes = line.split(",")
                title = (book_attributes[0].strip()).split(" ")[1]
                author = (book_attributes[1].strip()).split(" ")[1]
                publication_year = (book_attributes[2].strip()).split(" ")[2]
                genre = (book_attributes[3].strip()).split(" ")[1].strip()
                self.add_book_to_library(Book(title, author, publication_year, genre))
        except:
            print("An exception occurred")
