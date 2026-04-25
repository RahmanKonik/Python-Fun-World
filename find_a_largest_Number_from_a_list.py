
#date :- 10.04.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com

#First python program: find a largest number from a list.

#variable.

list_number = [12, 20, 3, 50, 62]
largest_number = 0
# or largest_number = list_number[0] # which is list_number[0] = 12 which value took from the list of number variable.

# largest number.

for largest in list_number:
    if largest > largest_number:
        largest_number = largest
print(f"Largest number is {largest_number} ")

# smallest number.
smallest_number = list_number[0]

for smallest in list_number:
    if smallest < smallest_number:
        smallest_number = smallest
print(f"Smallest number is {smallest_number} ")


print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===