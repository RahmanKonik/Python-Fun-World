

#date :- 21.04.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com

#First python program: Car game .

# variables.

user_command = ""
car_started = False

while True:

    user_command = input("> ").lower()

    if user_command == "start":

        if car_started:
            print("Car is already started!!!")
        else:
            car_started = True
            print("Car Started!!!")
    elif user_command == "stop":

        if not car_started:
            print("car already stopped!!!")
        else:
            car_started = False
            print("Car stopped!!!")

    elif user_command == "help":
        print("""Start: to start the car.
Stop: to stop the car.
Quit: quit the game.""")
    elif user_command == "quit":
        print("Quit the game!!!")
        break
    else:
        print("I donot understand it...")


print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===