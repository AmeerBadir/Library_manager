from library import Library
from book import Book


def main():
    msg = ("what you want to do, \n(add) adds books to library, \n(del) delete book from library,\n(edit) to edit book "
           "\n(display) to display the library books, \n(q) to exit\n")
    print("Welcome to Ameer Library")
    inp = input(msg)
    my_library = Library()
    while inp != "q":
        if inp == "add":
            title = input("insert book title ")
            author = input("insert book author ")
            publication_year = input("insert book publication year ")
            genre = input("insert book genre ")
            try:
                publication_year = int(publication_year)
                book = Book(title, author, publication_year, genre)
                my_library.add_book_to_library(book)
            except:
                print("adding failed")
                inp = input(msg)
                continue
        elif inp == "del":
            title = input("insert book title ")
            author = input("insert book author ")
            publication_year = input("insert book publication year ")
            genre = input("insert book genre ")
            try:
                publication_year = int(publication_year)
                book = Book(title, author, publication_year, genre)
                my_library.delete_book(book)
            except:
                print("deleting failed")
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
