 # The main objetive of this project is:
 # 1. Remove extra spaces
 # 2. Convert to lowercase
 # 3. Convert to uppercase
 # 4. Remove punctuation
 # 5. Remove numbers
 # 6. Replace a specific word
 # 7. Count words
 # 8. Exit

import string

# For better visualization

def back():
    input("\nPress Enter to go back to the menu.")

# 1. Remove extra spaces

def space(text):
    return text.strip()

# 2. Convert to lowercase

def lower(text):
    return text.lower()

# 3. Convert to uppercase

def upper(text):
    return text.upper()

# 4. Remove punctuation

def punctuation(text):
    table = str.maketrans("", "", string.punctuation)
    return text.translate(table)

# 5. Remove numbers

def digit(text):
    table = str.maketrans("", "", string.digits)
    return text.translate(table)

# 6. Replace a specific word

def replace(base, old, new):
    return base.replace(old, new)

# 7. Count words

def word(text):
    words = text.split()
    return len(words)

def main():
    while True:
        print("-------------------------")
        print("1. Remove extra spaces")
        print("2. Convert to lowercase")
        print("3. Convert to uppercase")
        print("4. Remove punctuation")
        print("5. Remove numbers")
        print("6. Replace a specific word")
        print("7. Count words")
        print("8. Exit")
        print("-------------------------\n")
        
        choice = input("Choose a number: ")
        
        if choice == "1":
            text = input("\nWhich text should the extra spaces be removed? ")
            print("\n-------------------")
            print(space(text))
            print("-------------------")
            back()
        elif choice == "2":
            text = input("\nWhich text should be converted to lowercase? ")
            print("\n-------------------")
            print(lower(text))
            print("-------------------")
            back()
        elif choice == "3":
            text = input("\nPlease insert a text to uppercase it: ")
            print("\n-------------------")
            print(upper(text))
            print("-------------------")
            back()
        elif choice == "4":
            text = input("\nPlease insert a text to remove it's punctuations: ")
            print("\n-------------------")
            print(punctuation(text))
            print("-------------------")
            back()
        elif choice == "5":
            text = input("\nInsert a text to remove it's digits: ")
            print("\n-------------------")
            print(digit(text))
            print("-------------------")
            back()
        elif choice == "6":
            base = input("\nInsert the base text: ")
            old = input("\nWhat would you want to replace? ")
            new = input("\nFor what? ")
            print("\n-------------------")
            print(replace(base, old, new))
            print("-------------------")
            back()
        elif choice == "7":
            text = input("\nInsert the text you want to count the words: ")
            print("\n-------------------")
            print(word(text))
            print("-------------------")
            back()
            
        # 8. Exit
            
        elif choice == "8":
            print("\n-------------------")
            print("Goodbye!")
            print("-------------------")
            break
        else:
            print("\nPlease choose one of the numbers.")
            back()
            
main()