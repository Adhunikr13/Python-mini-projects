import random
import sys


# lets set some variables
listOfWords = [
"Python","Scripting","Mississippi","Animal","Computer","Montreal"
           ]

word_guess = []
a = [x.lower() for x in listOfWords] #list comprehension to make sure it take 1st capital alpha 
secret = random.choice(a) # lets randomize single word from the list
Word_lenght= len(secret)
alpha = "abcdefghijklmnopqrstuvwxyz"
storage = []


def new():
    print("Welcome to Adhunik's Hangman!\n")

    while True:
        Choice = input("Would You Like to Play?\n").upper()

        if Choice == "YES" or Choice == "Y":
            break
        elif Choice == "NO" or Choice == "N":
            sys.exit("Exciting Game/.....")
        else:
            print("Please Answer only Yes or No")
            continue





def GameStart():

    for character in secret: # printing blanks for each letter in secret word
        word_guess.append("-")

    print("----------------------The word You need to guess has", Word_lenght, "characters--------------------")

    print("Be aware that You can enter only 1 letter from a-z\n\n")

    print(word_guess)



def Hangman():
    taken_guess = 1
    half = len(secret)/2
    while taken_guess <= half:


        guess = input("Pick a letter\n").lower()

        if not guess in alpha: #checking input
            print("Enter a letter from a-z alphabet")
        elif guess in storage: #checking if letter has been already used
            print("You have already guessed that letter!")
        else: 

            storage.append(guess)
            if guess in secret:
                print("You guessed correctly!")
                for x in range(0, Word_lenght): 
                    if secret[x] == guess:
                        word_guess[x] = guess
                        print(word_guess)

                if not '-' in word_guess:
                    print("You won!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                taken_guess += 1
                if taken_guess == half:
                    print("You lost! The secret word was",secret)

new()
GameStart()
Hangman()

print("Game Over!")

