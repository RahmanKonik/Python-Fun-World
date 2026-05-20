


#=================================
#date :- 20.05.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com
#=================================

# Python program: Shopping bill system.

items = []

while True:
    price = input("Enter the item prices ( type done ): ")

    if price.lower() == "done":
        break

    items.append(float(price))

total = sum(items)

print(f"Total bill is : {total}")



#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===