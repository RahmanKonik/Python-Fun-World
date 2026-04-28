
#date :- 27.04.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com

#First python program: user input a number  and program print that number in a string.

user_input_number = input("Phone Number: ")

# dictationary

digital_number_dictationay = {
    "0": "Null",
    "1": "Yksi",
    "2": "kaksi",
    "3": "Kolme",
    "4": "Neljä",
    "5": "Viisi",
    "6": "Kuusi",
    "7": "Seitsemän",
    "8": "Kahdeksan",
    "9": "Yhdeksän"
}

# storing the number in a variable.

output_digit = ""

# condition.

for charactor in user_input_number:
    output_digit += digital_number_dictationay.get(charactor, "!") + " "
print(f"String Number is : + {output_digit}")

print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===