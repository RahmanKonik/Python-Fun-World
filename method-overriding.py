

#=================================
#date :- 05.06.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com
#=================================

#python program: method overriding.

class Employee:

    def work(self):
        print("Employee is working.")

class Developer(Employee):
    def work(self):
        print("Developer is writing the code.")

class Manager(Employee):
    def work(self):
        print("Manager is managing the team.")

emp= Employee()
dev = Developer()

manage = Manager()

emp.work()
dev.work()
manage.work()


#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===