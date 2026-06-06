

#=================================
#date :- 06.06.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com
#=================================

#python program: student management system.

class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def show_student(self):
        print(f"Student details: name {self.name}, age: {self.age}, grade: {self.grade}")


student1 = Student("Rahman", 26, "A")

student1.show_student()

#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===