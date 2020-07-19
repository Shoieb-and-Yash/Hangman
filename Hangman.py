import random
from Words import *

def ChooseCateg():
    print("\n\n")
    print("Choose One of the Following Categories = ")
    print("1. Cars Brand Names")
    print("2. Bikes Brand Names")
    print("3. Tech Company Names")
    print("4. Country Names")
    print("5. Random Words(HARD LEVEL)")
    print("(Input numbers from 1-5 only)")
    choice = input();
    choice = int(choice);
    if(choice == 1):
        category = wordsCars
    elif(choice == 2):
        category = wordsBikes
    elif(choice == 3):
        category = wordsTech
    elif(choice == 4):
        category = wordsCountries
    elif(choice == 5):
        category = wordsHard
    else:
        print("Incorrect Input")
    return category

def ChooseWord(category):
    word = random.choice(category)
    return word.upper()

def Play(word):
    wordCompletion = "_" * len(word)
    hasGuessed = False
    guessedLetter = []
    guessedWords = []
    tries = 6

    print("Try and Guess the Right Word!")
    print(DisplayHangman(tries))
    print(wordCompletion)
    print("The Word has " + str(len(word)) + " Letters")

    while not hasGuessed and tries > 0:
        guess = input("Enter your Guess as a Letter or a Full word ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetter:
                print("You Already Guessed that Letter!")
            elif guess not in word:
                print(guess, " is not in the Word.")
                tries -= 1
                guessedLetter.append(guess)
            else:
                print(guess, " is in the Word!")
                wordAsList = list(wordCompletion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    wordAsList[index] = guess
                wordCompletion = "".join(wordAsList)
            if "_" not in wordCompletion:
                hasGuessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedWords:
                print("You have Already Guessed the Word!")
            elif guess != word:
                print(guess, "is not the Word")
                tries -= 1
                guessedWords.append(guess)
            else:
                hasGuessed = True
                wordCompletion = word
        else:
            print("Invalid Guess")
        print(DisplayHangman(tries))
        print("    ", wordCompletion)
        print("\n")
    if hasGuessed:
        print("Congratulations!! You Guessed it Right!")
    else:
        print("Whoops! You couldn't Guess the Word :/ ")
        print("The Correct Word was,", word)

def DisplayHangman(tries):
    stages = [  # Stage 6: Head, Torso, Left Arm, Right Arm, Left Leg, Right Leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # Stage 5: Head, Torso, Left Arm, Right Arm, Left Leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # Stage 4: Head, Torso, Left Arm, Right Arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # Stage 3: Head, Torso, Left Arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # Stage 2: Head and Torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # Stage 1: Head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # State 0: Empty
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]

def main():
    category = ChooseCateg()
    word = ChooseWord(category)
    Play(word)
    while input("Play Again? (Y/N) ").upper() == 'Y':
        category = ChooseCateg()
        word = ChooseWord(category)
        Play(word)

if __name__ == "__main__":
    main()
