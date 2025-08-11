list = []

def back():
    input("Press Enter to go back.")

def addTask(task):
    list.append(task)
    print("-------------------------")
    print(f"{task} has been added.")
    print("-------------------------")

def viewTasks():
    if not list:
        print("-------------------------")
        print("Your to-do list is empty.")
        print("-------------------------")
    else:
        print("Here's your to-do list: ")
        print("-------------------------")
        for i, task in enumerate(list, start=1):
            print(f"{i}. {task}")
        print("-------------------------")

def removeTask(index):
    try:
        list.pop(index - 1)
        print("-------------------------")
        print(f"Task {index} has been removed")
        print("-------------------------")
    except IndexError:
        print("-------------------------")
        print(f"{index} is not a valid task.")
        print("-------------------------")
        back()

def main():
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose a number: ")

        if choice == "1":
            task = input("Please enter a task: ")
            addTask(task)

        elif choice == "2":
            viewTasks()
            back()

        elif choice == "3":
            viewTasks()
            index = int(input("Select the number you intend to delete: "))
            removeTask(index)

        elif choice == "4":
            print("-------------------------")
            print("Goodbye!")
            break

        else:
            print(f"{choice} is not a valid option.")

main()