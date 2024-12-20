from typing import Dict, List
from project_library.user import User


class Library:

    def __init__(self):
        self.user_records: List[User] = []                          # User objects
        self.books_available: Dict[str: List[str]] = {}             # {'author': [books]
        self.rented_books: Dict[str: Dict[str: int]] = {}           # {'usernames': {'book_names': days_to_return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:

        if book_name in self.books_available[author]:                       # if book name in dict of available books
            self.books_available[author].remove(book_name)                  # remove book from available dictionary
            user.books.append(book_name)                                    # add book to user books list

            if user.username in self.rented_books:                              # if username in rented books dictionary
                self.rented_books[user.username][book_name] = days_to_return    # add book name to his username dict
            else:                                                               # if user not in rented books dictionary
                self.rented_books[user.username] = {book_name: days_to_return}  # create dictionary to his username

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for username, data in self.rented_books.items():
            if book_name in data:
                return f'The book "{book_name}" is already rented and will be available in {data[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User) -> [str, None]:
        if book_name in self.rented_books[user.username]:
            del self.rented_books[user.username][book_name]
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"
