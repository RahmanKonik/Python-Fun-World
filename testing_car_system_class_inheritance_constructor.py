
#date :- 10.04.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com

#First python program: testing two- car system .

class Car:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start(self):
        print(f"A {self.brand} is started")

    def drive(self):
        print(f"A {self.brand} car is running {self.speed} km/h")

    def stop(self):
        print(f"A {self.brand} car is stopped")

class ElectriCar(Car):
    def Battery(self):
        print(f"A {self.brand} 's battery is full charger")

car1 = Car("toyota","80")
car1.start()
car1.drive()
car1.stop()

tesla = ElectriCar("Tesla", "120")

tesla.start()
tesla.Battery()
tesla.drive()
tesla.stop()

print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===