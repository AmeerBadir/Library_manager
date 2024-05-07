from library import Library
from book import Book


def get_book_properties():
    title = input("insert book title ")
    author = input("insert book author ")
    publication_year = input("insert book publication year ")
    genre = input("insert book genre ")
    return title, author, publication_year, genre


def main():
    msg = ("what you want to do, \n(add) adds books to library, \n(del) delete book from library,\n(edit) to edit book "
           "\n(display) to display the library books, \n(q) to exit\n")
    print("Welcome to Ameer Library")
    inp = input(msg)
    my_library = Library()
    while inp != "q":
        if inp == "add":
            title, author, publication_year, genre = get_book_properties()
            try:
                publication_year = int(publication_year)
                book = Book(title, author, publication_year, genre)
                my_library.add_book_to_library(book)
            except:
                print("adding failed")
                inp = input(msg)
                continue
        elif inp == "del":
            title, author, publication_year, genre = get_book_properties()
            try:
                publication_year = int(publication_year)
                book = Book(title, author, publication_year, genre)
                my_library.delete_book(book)
            except:
                print("deleting failed")
                inp = input(msg)
                continue
        elif inp == "edit":
            title, author, publication_year, genre = get_book_properties()
            try:
                book_to_edit = Book(title, author, publication_year, genre)
                new_title = input("insert new title, if you dont want to change insert na ")
                new_author = input("insert new author, if you dont want to change the author insert na ")
                new_year = int(input("insert new year, if you dont want to change the year insert -1 "))
                new_genre = input("insert new genre, if you dont want to change the genre  insert na ")
                my_library.edit_book(book_to_edit, new_title, new_author, new_year, new_genre)
            except:
                print("editing failed")
                inp = input(msg)
                continue
        elif inp == "display":
            try:
                choose = input("(books) to display all books \n(genre) to display book by genre \n"
                               "(author) to display by author")
                if choose == "books":
                    my_library.display_library_books()
                elif choose == "genre":
                    book_genre = input("enter genre ")
                    my_library.display_book_by_gener(book_genre)
                elif choose == "author":
                    book_author = input("enter author ")
                    my_library.display_book_by_author(book_author)
            except:
                print("displaying failed")
                inp = input(msg)
                continue

        inp = input(msg)


if __name__ == '__main__':
    main()


