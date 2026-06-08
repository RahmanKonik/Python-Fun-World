

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

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_all_students(self):
        for student in self.students:
            student.show_student()
            print()


student1 = Student("Rahman", 26, "B")
student2 = Student("Alice", 27 ,"B")

school = School()

school.add_student(student1)
school.add_student(student2)

#student1.show_student()
#student1.update_grade("A")
#student1.show_student()

school.show_all_students()

#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===