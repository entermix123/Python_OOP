class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None


book1 = Book('The Hobbit', 'J.R.R. Tolki')
book1.page = 50
book2 = Book("blabla", "MF STFU")
book2.page = 100

library = Library()
library.add_book(book1)
library.add_book(book2)

found = library.find_book('blabla')
print(found.author)


