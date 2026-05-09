
#======================================
#date :- 07.05.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com
#======================================

#First python program: class method testing with car system.

class Car:

    def start(self):
        print("Car started")
    def stop(self):
        print("Car Stopped")
    def  gear(self, speed):
        if speed <= 10:
            print("Gear 1")
        elif speed <= 20:
            print("Gear 2")
        elif speed <= 30:
            print("Gear 3")
        else:
            print("Gear 4")

my_car = Car()

my_car.start()
speed = int(input("Enter a value of Speed: "))
my_car.gear(speed)
my_car.stop()


print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===