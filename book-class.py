

#=================================
#date :- 01.05.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com
#=================================

#First python program: book class with book details.

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_book_details(self):
        print(f"Books's title: {self.title}")
        print(f"Books's Author: {self.author}")
        print(f"Books's pages: {self.pages}")

    def is_long_book(self):
        if self.pages > 500:
            print(f"{self.title} is Long page book")
        else:
            print(f"{self.title} is short short page book")

book = Book ("Python Basics", "John Duc", 550)

book.show_book_details()
book.is_long_book()

#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===