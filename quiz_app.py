# Store a list of questions with multiple possible answers
# Ask the user each question one by one
# Lets the user choose an answer
# Checks if the answer is correct and gives immediate feedback
# Keeps track of the score
# Shows the final result at the end
# Extras:
# Random order of questions
# Highest score saving

# OBS: I could make questions based on themes that you could choose, but that's not the point of the project.

import random

# Questions

def quest_animal(answer = ""):
    print("\nWhat's the fastest animal in the world?")
    print("1- Peregrine falcon") #
    print("2- Cheetah")
    print("3- Sailfish")
    if answer == "1":
        return True
    else:
        return False
    
def quest_language(answer = ""):
    print("\nWhat's the most spoken language in the world?")
    print("1- Spanish")
    print("2- English")
    print("3- Mandarin Chinese") #
    if answer == "3":
        return True
    else:
        return False
    
def quest_planet(answer = ""):
    print("\nWhich planet is known as the Red Planet?")
    print("1- Venus")
    print("2- Mars") #
    print("3- Jupiter")
    if answer == "2":
        return True
    else:
        return False
    
def quest_ocean(answer = ""):
    print("\nWhat's the largest ocean on Earth?")
    print("1- Atlantic Ocean")
    print("2- Pacific Ocean") #
    print("3- Indian Ocean")
    if answer == "2":
        return True
    else:
        return False
    
def quest_olympics(answer = ""):
    print("\nIn which country did the Olympic Games originate?")
    print("1- Greece") #
    print("2- Italy")
    print("3- Egypt")
    if answer == "1":
        return True
    else:
        return False
    
def quest_desert(answer = ""):
    print("\nWhich is the largest desert in the world?")
    print("1- Sahara")
    print("2- Antarctic Desert") #
    print("3- Arabian Desert")
    if answer == "2":
        return True
    else:
        return False
    
def quest_river(answer = ""):
    print("\nWhat's the longest river in the world?")
    print("1- Nile") #
    print("2- Amazon")
    print("3- Yangtze")
    if answer == "1":
        return True
    else:
        return False
    
def quest_monalisa(answer = ""):
    print("\nWho painted the Mona Lisa?")
    print("1- Vincent van Gogh")
    print("2- Leonardo da Vinci") #
    print("3- Pablo Picasso")
    if answer == "2":
        return True
    else:
        return False
    
def quest_worldwar(answer = ""):
    print("\nIn which year did World War II end?")
    print("1- 1950")
    print("2- 1939")
    print("3- 1945") #
    if answer == "3":
        return True
    else:
        return False
    
def quest_symbol(answer = ""):
    print("\nWhat's the chemical symbol for gold?")
    print("1- Au") #
    print("2- Ag")
    print("3- Go")
    if answer == "1":
        return True
    else:
        return False
    
def quest_genetic(answer = ""):
    print("\nWhich part of the cell contains genetic material?")
    print("1- Nucleus") #
    print("2- Cytoplasm")
    print("3- Mitochondria")
    if answer == "1":
        return True
    else:
        return False
    
def quest_pop(answer = ""):
    print('\nWho is known as the "King of Pop"?')
    print("1- Elvis Presley")
    print("2- Michael Jackson") #
    print("3- Prince")
    if answer == "2":
        return True
    else:
        return False
    
def quest_quote(answer = ""):
    print('\nWhich movie features the quote “I’ll be back”?')
    print("1- Predator")
    print("2- Rambo")
    print("3- The Terminator") #
    if answer == "3":
        return True
    else:
        return False
    
def quest_rainbow(answer = ""):
    print("\nHow many colors are in the rainbow?")
    print("1- 6")
    print("2- 7") #
    print("3- 8")
    if answer == "2":
        return True
    else:
        return False
    
def quest_flower(answer = ""):
    print("\nWhat’s the national flower of Japan?")
    print("1- Rose")
    print("2- Cherry Blossom") #
    print("3- Lotus")
    if answer == "2":
        return True
    else:
        return False
    
# List of the questions
    
questions = [
    quest_animal,
    quest_language,
    quest_planet,
    quest_ocean,
    quest_olympics,
    quest_desert,
    quest_river,
    quest_monalisa,
    quest_worldwar,
    quest_symbol,
    quest_genetic,
    quest_pop,
    quest_quote,
    quest_rainbow,
    quest_flower
]

while True:
    question = random.choice(questions)
    question()
    answer = input("\nAnswer:")
    if question(answer) == True:
        print("\n---------------")
        print("Right Answer!")
        print("---------------")
        input("")
    else:
        print("\n---------------")
        print("Sorry, wrong answer!")
        print("---------------")
        input("")
    questions.remove(question)
    if questions:
        continue
    else:
        print("Test")
        break
