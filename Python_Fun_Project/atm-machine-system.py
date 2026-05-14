
#date :- 10.04.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com

#=====================================

# python program: ATM machine system .

user_name = str(input("Enter your serect name: ")).lower()

def user_account():

    Balance = 1000

    while True:
        print("""
1.Check Balance
2.Deposit
3.Withdrew
4.Exit
""")
        choice = input("Your selection number:")

        if choice == "1":
            print(f"Name : {user_name}")
            print("Account Number: XXXXXXXXX123")
            print(f"Your balance is {Balance} euro")
        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            Balance = Balance + amount
            print("Deposit is added successfully")
            print(f"Now your balance is {Balance}")
        elif choice == "3":
            amount = int(input("Enter your withdrew amount: "))
            if amount > Balance:
                print("Insufficient Balance.")
            else:
                Balance = Balance - amount
                print("Withdrew successfully")
                print(f"Now your balance is {Balance}")
        elif choice == "4":
            print("Thank you for your")
            break
        else:
            print("Invalid Number...")

if user_name == 'konik':
    print(f"Hi, {user_name}. Welcome back...")
    user_account()
else:
    print(f"Sorry, not find this {user_name} name account in our system.")


print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===