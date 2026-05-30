

#=================================
#date :- 31.05.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com
#=================================

#First python program: testing a employee class method for employee information.

class Employee:

    def __init__(self, name , salary):

        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee name is {self.name} and salary is {self.salary}.")

    def salary_increase(self, amount):
        print(f"Current salary was {self.salary}")
        self.salary += amount
        print(f"after salary increase {amount}, salary now : {self.salary}")


employee1 = Employee("Rahman", 2000)

employee1.show_details()
employee1.salary_increase(500)
employee1.show_details()

#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===