class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def add_book(self, title):
        if title in self.books:
            print(f"This book already on the shelf!!!")
        else:
            self.books.append(title)
            print(f"The book '{title}' was placed on the shelf")

    def show_books(self):
        print(f"There is a list of all books: {', '.join(self.books)}")

    def find_book(self, title):
        if title in self.books:
            print(f"The book from the shelf: {title}")
        else:
            print(f"You make a mistake. There is no such book on the shelf like {title}")

first_shelf = Library(["Niger1", "Beyond the Niger", "The Mars"])
first_shelf.add_book("Brothers")
first_shelf.add_book("Brothers")
first_shelf.show_books()
first_shelf.find_book("Brothers")

