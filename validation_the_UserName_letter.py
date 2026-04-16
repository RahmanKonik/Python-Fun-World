
#date :- 16.04.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com

#First python program: print a statement which is validation the user input name depend on it length.


user_name = input("Enter your name: ")

user_name_length = len(user_name)
print(f"user name length is : {user_name_length}")

if user_name_length < 3:
    print("User name must be at least 3 characters.")
elif user_name_length > 50:
    print("User name can be more than 50 characters.")
else:
    print("User name looks good.")


print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===