

#=================================
#date :- 04.06.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com
#=================================

#First python program: inheritance class( one class(attribute and method) reuse in another class).

class Vehicle:

    def __init__(self, brand):
        self.brand = brand
    def show_brand(self):
        print(f"Brand: ", self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def show_car(self):
        print(f"Model: ", self.model)
class Bike(Vehicle):
    def __init__(self, brand, bike_type):
        super().__init__(brand)
        self.bike_type = bike_type
    def show_bike(self):
        print(f"Bike_type: ", self.bike_type)


car1 = Car("Toyota", "Yaris")

car1.show_brand()
car1.show_car()

bike1 = Bike("Yamaha", "Sports")

bike1.show_brand()
bike1.show_bike()

#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===