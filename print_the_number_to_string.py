
#date :- 27.04.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com

#First python program: user input a number  and program print that number in a string.

user_input_number = input("Number: ")

# dictationary

digital_number_dictationay = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

# storing the number in a variable.

output_digit = ""

# condition.

for charactor in user_input_number:
    output_digit += digital_number_dictationay.get(charactor, "!") + " "
print(f"String Number is : {output_digit}")

print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===