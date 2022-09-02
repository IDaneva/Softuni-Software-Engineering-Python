searched_book = input()

books_that_she_went_through = 0

while True:
    book_name = input()

    if book_name == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_that_she_went_through} books.")
        break

    if book_name == searched_book:
        print(f"You checked {books_that_she_went_through} books and found it.")
        break

    books_that_she_went_through += 1
