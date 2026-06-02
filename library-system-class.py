

#=================================
#date :- 02.06.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com
#=================================

#First python program: library system.

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):

        self.books.append(book)
        print(book, " Booked added.")

    def borrow_book(self, book):
        if book in self.books:
            for book in self.books:
                self.books.remove(book)
                print(book, " Booked removed.")
        else:
            print("Book not found.")

    def show_books(self):
        for book in self.books:
            print("- ", book)

library = Library()

library.add_book("Python Basics")
library.add_book("Java Programming Languages")
library.show_books()

library.borrow_book("Python Basics")
library.show_books()

library.add_book("C++ ")
library.show_books()

library.borrow_book("React")
library.show_books
#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===