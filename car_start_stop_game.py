

#date :- 18.04.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com

#First python program: car game ( start , stop or quite the game ) in python.


#all variables.

user_command = ""
started = False

while True:

    user_command= input("> ").lower()
    if user_command == "start":
        if started:
            print("Car is already started!.")
        else:
            started= True
            print("Car is Started, car is going...")
    elif user_command == "stop":

        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car is Stopped, car stopped...")
    elif user_command == "help":
        print("""Start: to start the car...
                Stop: to stop the car...
                Quite: to quite the game
              """)
    elif user_command == "quite":
        print("It's quite!")
        break
    else:
        print("Anteeksi, En ymmärrä!...")


print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===