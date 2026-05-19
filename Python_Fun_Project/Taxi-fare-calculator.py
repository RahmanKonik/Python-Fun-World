

#=================================
#date :- 10.04.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com
#=================================

#First python program: taxi fare or payment calculating calculator.

basic_rate = 5
per_km_rate = 1.5

distance = int(input("Enter your distance: "))

if distance < 5:
    customer_rent = basic_rate + ( 1 * distance )
else:
    customer_rent = basic_rate + ( per_km_rate * distance )

print(f"Customer Rent is {customer_rent} on this {distance} km")
print("Thank you for choicing our servicing...")


#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===