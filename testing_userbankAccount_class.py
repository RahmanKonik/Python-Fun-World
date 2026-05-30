

#=================================
#date :- 30.05.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com
#=================================

#First python program: Testing the class method with user bank account system information.


class BankAccount:

    def __init__(self, owner, balance):
        self.balance = balance
        self.owner = owner

    def deposite(self, amount):
        self.balance += amount
        print(f" {amount} deposited successful")
        print(f" Now, Total balance is {self.balance}")

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print(f" {amount} withdrawn successful")
            print(f" Now, Total balance is {self.balance}")
        else:
            print("Balance insufficient!")
            print(f" Your current balance is {self.balance}.")

    def show_balance(self):
        print(f" {self.owner}'s balance is : {self.balance}")

ace1 = BankAccount("konik", 1000)

ace1.show_balance()
ace1.deposite(500)
ace1.withdraw(1700)


#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===