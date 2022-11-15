#Isaiah Gocool
#ICS2O
#June 10, 2019
#A computer software themed Hangman game
import random
print("Welcome to Hangman!")
print("RULES")
print("Please make sure all of your answers are lowercase letters")
print("Any spaces in the word you are trying to guess will have to be indicated with a dash (-).")
print("Type in \"hint\" for a hint.")
print("Do not make your guesses more than 1 character.")
print("Maximize the window for the best experience possible.")
playAgain = "yes"
while(playAgain == "yes"): #Restarts the game when playAgain == "Yes"
    list1 = ["microsoft-word", "minecraft", "steam", "spotify", "google-drive", "gimp", "powerpoint", "photoshop", "discord", "instagram"]
    num = int(random.randint(0, 9))
    word = str(list1[num])
    lenWord = int(len(word))
    blank = str("_"*lenWord)
    guess = 0
    wordBank = []
    blank2 = ("_"*lenWord)
    win = 0
    while(guess < 6 and win != 1): #Allows the user to keep on entering a guess until there are 6
        userLetter = str(input("Enter a letter: "))
        userLetter = userLetter.lower()
        lenUser = int(len(userLetter))
        check = 0
        if(lenUser > 1 and userLetter != "hint"): #Penalizes the user for using a word as a guess
            guess = (guess + 1)
            print("Please make your guess a letter!")
        if(userLetter == "hint" and num == 0): #Gives the hint for "microsoft-word"
            print("It was originally released by Microsoft in 1983 for Xenix systems.")
        if(userLetter == "hint" and num == 1): #Gives the hint for "minecraft"
            print("This popular video game was released on May 17, 2009.")
        if(userLetter == "hint" and num == 2): #Gives the hint for "steam"
            print("There are nearly 90 million active users on this platform.")
        if(userLetter == "hint" and num == 3): #Gives the hint for "spotify"
            print("This software was created by Daniel Ek and Martin Lorentzon.")
        if(userLetter == "hint" and num == 4): #Gives the hint for "google-drive"
            print("The desktop app shut-down on December 11, 2017.")
        if(userLetter == "hint" and num == 5): #Gives the hint for "gimp"
            print("The code was written in C.")
        if(userLetter == "hint" and num == 6): #Gives the hint for "powerpoint"
            print("This software was initially exclusive to Macintosh computers.")
        if(userLetter == "hint" and num == 7): #Gives the hint for "photoshop"
            print("This software was developed by Adobe.")
        if(userLetter == "hint" and num == 8): #Gives the hint for "discord"
            print("The target audience is gamers.")
        if(userLetter == "hint" and num == 9): #Gives the hint for "instagram"
            print("This service is currently owned by Facebook, Inc.")
        while(check < lenWord and lenUser == 1): #Checks to see if the user's guess is one of the characters in the word
            if(userLetter == (word[check]) and lenUser == 1): #If the user's letter is one of the characters in the word, it will add it to the blank word-box
                blank = str(blank[0:check]+userLetter+blank[check+1:lenWord])
                blank2 = str(blank2[0:check]+userLetter+blank2[check+1:lenWord])
            check = (check + 1)
        if(blank2 == ("_"*lenWord) and lenUser == 1): #If the user's letter is not one of the characters in the word, they will have less guesses left
            guess = (guess + 1)
            wordBank.append(userLetter)
        blank2 = ("_"*lenWord)
        if(guess == 0): #Displays the graphic when the user has 6 guesses left
            print("           _______")
            print("           |     |")
            print("           |      ")
            print("           |      ")
            print("           |      ")
            print("           |      ")
            print("        ----------")
            print("The word is:" , blank)
            print("You have used the letters:" , wordBank)
        elif(guess == 1): #Displays the graphic when the user has 5 guesses left
            print("           _______")
            print("           |     |")
            print("           |  (° ͜°)")
            print("           |      ")
            print("           |      ")
            print("           |      ")
            print("        ----------")
            print("The word is:" , blank)
            print("You have used the letters:" , wordBank)
        elif(guess == 2): #Displays the graphic when the user has 4 guesses left
            print("           _______")
            print("           |     |")
            print("           |  (° ͜°)")
            print("           |     |")
            print("           |      ")
            print("           |      ")
            print("        ----------")
            print("The word is:" , blank)
            print("You have used the letters:" , wordBank)
        elif(guess == 3): #Displays the graphic when the user has 3 guesses left
            print("           _______")
            print("           |     |")
            print("           |  (° ͜°)")
            print("           |    /|")
            print("           |      ")
            print("           |      ")
            print("        ----------")
            print("The word is:" , blank)
            print("You have used the letters:" , wordBank)
        elif(guess == 4): #Displays the graphic when the user has 2 guesses left
            print("           _______ ")
            print("           |     | ")
            print("           |  (° ͜°)")
            print("           |    /|\ ")
            print("           |       ")
            print("           |       ")
            print("        ---------- ")
            print("The word is:" , blank)
            print("You have used the letters:" , wordBank)
        elif(guess == 5): #Displays the graphic when the user has 1 guess left
            print("           _______ ")
            print("           |     | ")
            print("           |  (° ͜°)")
            print("           |    /|\ ")
            print("           |    /  ")
            print("           |       ")
            print("        ---------- ")
            print("The word is:" , blank)
            print("You have used the letters:" , wordBank)
        elif(guess == 6): #Displays the graphic when the user has no guesses left
            print("           _______ ")
            print("           |     | ")
            print("           |  (° ͜°)")
            print("           |    /|\ ")
            print("           |    / \ ")
            print("           |       ")
            print("        ---------- ")
            print("You have lost!  The word was:" , word)
        if(blank == word): #Displays the message when the user has won
            print("Congratulations, you have won!")
            win = 1
            playAgain = 0
    playAgain = str(input("Would you like to play again?  Please type \"yes\" if you would like to. ")) #If the user inputs "Yes", the game restarts
    playAgain = playAgain.lower()
print("Thank you for playing! :D")
