
#date :- 10.04.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com

#First python program: try exception testing in python.
try:
    age = int(input("Age: > "))

    person = 12
    risk = person / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero !")
except ValueError:
    print("Invalid Input!")



print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===