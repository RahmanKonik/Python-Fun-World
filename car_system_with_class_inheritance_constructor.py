
#date :- 10.05.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com

#First python program: car system demo testing with class, inheritance and constructor method.

# parent class

class Car:

    # constructor.
    def __init__(self, brand, speed):

        self.brand = brand
        self.speed = speed
    def drive(self):
        print(f"a {self.brand} is driving in {self.speed} km/h")

    def stop(self):
        print(f"A {self.brand} is stopped")
# inheritance

class ElectriCar(Car):
    def battery(self):
        print("battery is full charger!")


car1 = Car("Toyata", "80")
car1.drive()

# object from child class

tesla = ElectriCar("Tesla", "120")

tesla.drive()
tesla.battery()

toyota = ElectriCar("Toyota", "200")

toyota.drive()
toyota.battery()
toyota.stop()

print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===