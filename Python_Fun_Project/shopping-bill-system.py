


#=================================
#date :- 20.05.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com
#=================================

# Python program: Shopping bill system.

items = []
count = 0

print("=== Welcome to the shop bill System ===")

while True:

    name = input("Please enter the item name ( Or type Done ): ")

    if name.lower() == "done":
        break
    price = float(input("Enter the item prices: "))

    items.append((name, price))
    count += 1

 # total = sum(items)

total = 0

print("=== Receipt ===")
print("=== Date ===")

for item in items:
    print(f"{item[0]} price - £{item[1]}")
    total = total + item[1]

print("=====================")
print(f"Bill is {count} item and price is {total}")



print(f"Total bill of {count} is : {total}")



#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===