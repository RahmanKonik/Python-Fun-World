
#date :- 06.05.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com

#First python project: Smart cart control system project.

# Smart Car Control System.

car_system_started = False


def car_gear_control_function(speed):

    if speed == 0:
        return "Car is not moving."
    elif speed <= 10:
        return "Car is moving  and Gear number 2."
    elif speed <= 20:
        return "Gear 2"
    elif speed <=30:
        return "Gear 3"
    else:
        return "Gear 4 or 5 more than..."

while True:

    command = input("Enter your help: ").lower()

    if command == "start":
        if car_system_started:
            print("Car already started!")
        else:
            car_system_started = True
            print("Car started...")

    elif command == "stop":
        if not car_system_started:
            print("Car already stopped!")
        else:
            car_system_started = False
            print("Car stopped!")

    elif command == "speed":

        if not car_system_started:
            print("Please, start the car first!")
            continue

        try:
            speed = int(input("Enter a speed: "))

            if speed < 0:
                print(" Speed cannot be negative!")
            else:
                gear = car_gear_control_function(speed)
                print(f"Car speed {speed} & gear {gear}")
        except ValueError:
            print("Invalid Number, Please enter a valid number.")
        except TypeError:
            print(" Please type correctly, thank!")

    elif command == "help":
        print("""
start: to start the car
stop : to stop the car
speed: to input the speed & get the gear number.
quit : to quit the system.
""")
    elif command == "quit":
        print("off the car control system!")
        break
    else:
        print("Unkown command for System!")





print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===