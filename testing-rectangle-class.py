

#=================================
#date :- 31.05.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com
#=================================

#First python program: find the area and parameter by rectangle class.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        total_area = self.length * self.width
        print(f"Area is : {total_area}")

    def perimeter(self):
        total_perimeter = 2 * ( self.length + self.width)
        print(f"Perimeter is : {total_perimeter}")

rectangle1 = Rectangle(10, 5)

rectangle1.area()
rectangle1.perimeter()

#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===