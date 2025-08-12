# Main objetive:
# 1. Add contact
# 2. View contacts
# 3. Search contact
# 4. Edit contact
# 5. Delete contact
# 6. Exit

dic = {}

# For better visualization

def back():
    input("\nPress Enter to go back to the menu.")
        
# Check if the name is valid to use

def checkName(name):
    for char in name:
        if name.isalpha() == False or name.strip() == "":
            return False
        else:
            return True

# Check if the number is valid

def checkNumber(number):
    for char in number:
        if number.isdigit() == False and number != "-" or number.strip() == "":
            return False
        else:
            return True

# 1.

def addContact(name, number=""):
    checkName(name)
    dic[name] = number
    print("-------------------------------")
    print(f"{name} has been added to your contacts.")
    print("-------------------------------")
    

# 2.

def viewContacts():
    if dic:
        print("\nHere's your list of contacts: ")
        print("-------------------------------")
        for name, number in dic.items():
            print(f"{name}: {number}")
        print("-------------------------------")
    else:
        print("\n-------------------------------")
        print("You don't have a contact list yet.")
        print("-------------------------------")

# 3.

def searchContact(name):
    if name in dic:
        print("\n-------------------------------")
        print(f"{name}'s number is {dic[name]}")
        print("-------------------------------")
    elif name.strip() == "":
        cancel = input("\nPlease insert a name. If you want to cancel just press Enter. ")
        if cancel.strip() == "":
            main()
        else:
            searchContact(cancel)
    else:
        print("\n-------------------------------")
        print(f'The name "{name}" is not in your contact list')
        print("-------------------------------")

# 4.

def editContact(name):
    if name in dic:
        print("\n-------------------------------")
        print(f"Their phone number is: {dic[name]}")
        print("-------------------------------")
        new_number = input("\nWhat should their new phone number be? ")
        dic[name] = new_number
        print("\n-------------------------------")
        print(f"{name}'s phone number has been updated.")
        print("-------------------------------")
    elif name.strip() == "":
        cancel = input("Please insert a name. If you want to cancel it just press Enter. ")
        if cancel.strip() == "":
            main()
        else:
            searchContact(cancel)
    else:
        print("\n-------------------------------")
        print(f"{name} is not in your contacts.")
        print("-------------------------------")

# 5.

def deleteContact(name):
    if name in dic:
        dic.pop(name)
        print("\n-------------------------------")
        print(f"{name} has been remove from your contacts list.")
        print("-------------------------------")
    elif name.strip() == "":
        cancel = input("\nPlease insert a name. If you want to cancel it just press Enter. ")
        if cancel.strip() == "":
            main()
        else:
            deleteContact(cancel)
    else:
        print("\n-------------------------------")
        print(f"{name} is not in your contacts list.")
        print("-------------------------------")

def main():
    while True:
        print("---------------------")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Edit contact")
        print("5. Delete contact")
        print("6. Exit")
        print("---------------------\n")

        choice = input("Choose a number: ")

        if choice == "1":
            name = input("\nInsert a name: ")
            number = input("Enter their number: ")
           
            # Checking if both are valid inputs

            if checkName(name) and checkNumber(number):
                addContact(name, number)
                back()
            elif checkName(name) == False and checkNumber(number) == True:
                print("\n-------------------------------")
                print(f"{name} is not a valid name.")
                print("-------------------------------")
                back()
            elif checkName(name) == True and checkNumber(number) == False:
                print("\n-------------------------------")
                print(f"{number} is not a valid number.")
                print("-------------------------------")
                back()
            else:
                print("\n-------------------------------")
                print("Those are not valid inputs!")
                print("-------------------------------")
                back()
        
        elif choice == "2":
            viewContacts()
            back()
       
        elif choice == "3":    
            name = input("Who would you like to search for? ")
            searchContact(name)
            back()
       
        elif choice == "4":
            name = input("Who's contact would you want to change? ")
            editContact(name)
            back()
        
        elif choice == "5":
            name = input("Who would you like to remove from your contacts list? ")
            deleteContact(name)
            back()
       
        elif choice == "6":
            break
        
        else:
            print("\n---------------------")
            print("Please select one of the numbers.")
            print("---------------------")
            back()


main()