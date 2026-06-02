

#=================================
#date :- 02.05.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com
#=================================

#First python program: shopping cart class.

class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_items(self, item):
        self.items.append(item)
        print(item," Item added...")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(item," item removed...")
        else:
            print("Item not found!")

    def show_items(self):
        print("items in shopping cart: ")

        for item in self.items:
            print("- ", item)


cart = ShoppingCart()

cart.add_items("Milk")
cart.add_items("Bread")
cart.add_items("Eggs")
cart.show_items()
cart.remove_item("Bread")
cart.show_items()

#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===