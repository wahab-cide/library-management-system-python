#create book class and initialize params
class Book:
    def __init__(self, book_title, book_author, isbn_number):
        self.book_title = book_title
        self.book_author = book_author
        self.isbn_number = isbn_number
        self.is_available = True

    def display_info(self):
        print(f"Title: {self.book_title}\nAuthor: {self.book_author}\nISBN Number: {self.isbn_number}\nAvailable: {'Yes' if self.is_available else 'No'}\n")

#create library class and add methods
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.book_title}' added to the library.")

    def display_books(self):
        print("List of Library Books:")
        for book in self.books:
            book.display_info()

    def lend_book(self, book_title):
        for book in self.books:
            if book.book_title == book_title and book.is_available:
                book.is_available = False
                print(f"Book '{book_title}' has been lent.")
                return
        print(f"Sorry, '{book_title}' is either not available or does not exist in the library.")

    def return_book(self, book_title):
        for book in self.books:
            if book.book_title == book_title and not book.is_available:
                book.is_available = True
                print(f"Book '{book_title}' has been returned.")
                return
        print(f"Sorry, '{book_title}' cannot be returned. Check the book title or availability.")

    def available_books(self):
        return [book for book in self.books if book.is_available]

    def display_current_books(self):
        current_books = self.available_books()
        if not current_books:
            print("No books currently available in the library.")
        else:
            print("\nCurrent Books in the Library:")
            for book in current_books:
                book.display_info()
