from user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        # author: [list of available books]
        self.rented_books = {}
        # username: {book_name: days left to return to the library}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available[author]:
            user_dict = {book_name: days_to_return}
            self.rented_books[user.username] = {}
            self.rented_books[user.username].update(user_dict)
            self.books_available[author].remove(book_name)
            user.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        else:
            for users, info in self.rented_books.items():
                for title, date in info.items():
                    if title == book_name:
                        return f"The book \"{book_name}\" is already rented and will be available in {date} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]

        return f"{user.username} doesn't have this book in his/her records!"
