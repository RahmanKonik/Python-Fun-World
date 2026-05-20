


#=================================
#date :- 20.05.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com
#=================================

# Python program: Shopping bill system.

items = []
count = 0

while True:
    price = input("Enter the item prices ( type done ): ")

    if price.lower() == "done":
        break

    items.append(float(price))
    count += 1

total = sum(items)

print(f"Total bill of {count} is : {total}")



#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===