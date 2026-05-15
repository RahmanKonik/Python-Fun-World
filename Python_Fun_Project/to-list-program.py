


#=================================
#date :- 15.05.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com
#=================================

#First python program: To-do sytem program for user daily note.

tasks = []

while True:

    print("""
1. Add a New List.
2. View your list.
3. Remove a list.
4. Exit
""")
    choice = input("Selection Number: ")

    if choice == "1":

        task = input("Your Task is : ")
        tasks.append(task)
        print("Task added successfully. Thank you!")

    elif choice == "2":
        print("Your List is : \n")

        if len(tasks) == 0:
            print("No task exists!")
        else:
            for task in tasks:
              print("=> ", task)
    elif choice == "3":

        if len(tasks) == 0:
            print("No task exist for removing...")
        else:
            print("\n Current task: ")
            for task in tasks:
                print("-> ", task)

            remove_task = input("Enter task name to remove: ")

            if remove_task in tasks:
                tasks.remove(remove_task)
                print(f"The {remove_task} has been removed.")
            else:
                print("Task not found.")

    elif choice == "4":
        print("Thank you and GoodBye...")
        break
    else:
        print(f"Invalid Number, {choice} .")


#=================================
print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===