

#=================================
#date :- 28.05.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com
#=================================

#First python program: Create a student class and testing it by printing some student information.


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_info_show(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

student1 =Student("Konik", "29")

student1.student_info_show()

#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===