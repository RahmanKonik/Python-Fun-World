

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

    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"{new_grade}, grade is updated")



student1 = Student("Rahman", 26, "B")

student1.show_student()
student1.update_grade("A")
student1.show_student()

#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===