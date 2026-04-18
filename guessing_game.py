
#date :- 18.04.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com

#First python program: guessing game in python.


#all variables.

secret_number = 6
guess_counter = 1
guess_limitation = 3

# while loop and if condition.

while guess_counter <= guess_limitation:
    guess = int(input("Your guess Number: "))
    guess_counter += 1
    # if condition part.
    if guess == secret_number:
        print(" Your won!")
        break
else:
    print("Anteeksi, Your Failed!")

print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===