

#date :- 21.04.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com

#First python program: version-1.0: car speed game .


# variables.

command = ""
car_started = False

while True:
    command = input(">").lower()

    if command == "start":
        if car_started:
            print("Car already started")
        else:
            car_started = True
            print("Car Started")
    elif command == "stop":
        if not car_started:
            print("Car already stopped!")
        else:
            car_started = False
            print("car stopped")
    elif command == "speed":
        if not car_started:
            print("Start the car first, then change the gear!")
        else:
            speed = int(input(">>"))
            if speed < 0:
                print("Speed cannot be negative!")
            else:
                if speed == 0:
                    print("Car is not moving.")
                elif speed <= 20:
                    print("Use Gear 1")
                elif speed <= 40:
                    print("Use Gear 2")
                elif speed <= 60:
                    print("Use Gear 3")
                elif speed <= 80:
                    print("Use Gear 4")
                else:
                    print("Use Gear 5")

    elif command == "help":
        print("""start: to start the car.
              stop: to stop the car.
              quit: to quit the game""")
    elif command == "quit":
        print("quit the game.")
        break
    else:
        print("Anteeksi, En ymmarra!!")



print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===