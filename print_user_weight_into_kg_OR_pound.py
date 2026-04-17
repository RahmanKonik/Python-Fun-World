

#date :- 17.04.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com

#First python program: print the user weight into kilogram or pound after user input the weight and selecting a unit, kilo (L) or pound(k).

user_weight = int(input("Enter your weight: "))
user_value_unit = input("What unit you have, is it pounds(L) or kilos (k): ")

# which unit value do you want to see. selecting in here.
weight_unit = input("what unit do you want (L)bs or (k)g . ")

# condition
print(f"User input value's unit is {user_value_unit}")

if user_value_unit.upper() == "K" and weight_unit.upper() == "L":
    convertor = user_weight * 2.20462
    print(f"User weight is {convertor} lbs")
elif weight_unit.upper() == "K" and user_value_unit.upper() == "L":
    convertor = user_weight / 2.20462
    print(f"User weight is {convertor} kilos")
else:
    print("Invalid input")


print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===