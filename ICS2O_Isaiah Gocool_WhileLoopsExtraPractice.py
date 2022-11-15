#Isaiah Gocool
#ICS2O
#March 29, 2019
#While loops extra practice questions
num1 = int(input("Enter the first number greater than 1: "))
while(num1 < 1):
    num1 = int(input("Enter the first number greater than 1: "))
num2 = int(input("Enter the second number greater than 1: "))
while(num2 < 1):
    num2 = int(input("Enter the second number greater than 1: "))
if(num1 < num2):
    if((num2 - num1) < 4):
        print("The numbers are not 3 apart.")
        while ((num2 - num1) < 4):
            num1 = int(input("Enter the first number greater than 1: "))
            num2 = int(input("Enter the second number greater than 1: "))
    while(num1 < (num2 - 1)):
        num1 = (num1 +2)
        print(num1)
else:
    if((num1 - num2) < 4):
        print("The numbers are not 3 apart.")
        while ((num1 - num2) < 4):
            num1 = int(input("Enter the first number greater than 1: "))
            num2 = int(input("Enter the second number greater than 1: "))
    while(num2 < (num1 - 1)):
        num2 = (num2 + 2)
        print(num2)
print("################################################################################")
#Isaiah Gocool
#ICS2O
#March 30, 2019
#Program determines the percent of marks above 70%
mark = int(input("Enter a mark: "))
count = 0
mark70 = 0
while(mark != -1):
    mark = int(input("Enter a mark: "))
    count = (count + 1)
    if(mark > 70):
        mark70 = (mark70 + 1)
if mark == -1:
    print(mark70/count*100,"% of the marks are over 70%")
print("################################################################################")
#Isaiah Gocool
#ICS2O
#March 31, 2019
#Calculates the factorial of a number
factorial = 1
num = int(input("Enter a number greater than 0: "))
while(num > 0):
    factorial = factorial * num
    num = (num - 1)
print(factorial)
print("Goodbye")
print("################################################################################")
#Isaiah Gocool
#ICS2O
#March 31, 2019
#Tells the user when they should wake up
num = 50
while(num > 0):
    num = int(input("What is the day of the week? "))
    if(num == 2 or num == 4 or num == 6):
        print("You need to wake up at 7am.")
    elif(num == 1 or num == 7 or num == 8):
        print("You should sleep in.")
    elif(num == 3 or num == 5):
        print("You need to wake up at 8am.")
print("################################################################################")
#Isaiah Gocool
#ICS2O
#March 31, 2019
#Asks the user for two integers
num1 = 1
num2 = 2
while not(num1 == 0 and num2 == 0):
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    if(num1 != num2):
        print("The sum is:" , num1+num2)
    if(num1 == num2):
        print("Double the sum is:" , (num1+num2)*2)
print("################################################################################")
#Isaiah Gocool
#ICS2O
#March 31, 2019
#Gives the user points depending on the number they input
import random
playAgain = 1
randNum = 1
num = 0
count = 0
randNum = int(random.randint(1, 50))
num = int(input("Guess the integer between 1 and 100: "))
if(num + 10 == randNum or num - 10 == randNum):
    count = count + 2
    print("Good job!  You have a score of" , count)
    playAgain = int(input("Would you like to play again?  Press 1 to play again! "))
elif(num + 5 == randNum or num - 5 == randNum):
    count = count + 4
    print("Wow!  You have a score of" , count)
    playAgain = int(input("Would you like to play again?  Press 1 to play again! "))
elif(num + 2 == randNum or num - 2 == randNum):
    count = count + 6
    print("AMAZING!  You have a score of" , count)
    playAgain = int(input("Would you like to play again?  Press 1 to play again! "))
while(playAgain == 1):
    randNum = int(random.randint(1, 100))
    num = int(input("Guess the integer between 1 and 100: "))
    if(num + 10 == randNum or num - 10 == randNum):
        count = count + 2
        print("Good job!  You have a score of" , count)
        playAgain = int(input("Would you like to play again?  Press 1 to play again! "))
    elif(num + 5 == randNum or num - 5 == randNum):
        count = count + 4
        print("Wow!  You have a score of" , count)
        playAgain = int(input("Would you like to play again?  Press 1 to play again! "))
    elif(num + 2 == randNum or num - 2 == randNum):
        count = count + 6
        print("AMAZING!  You have a score of" , count)
        playAgain = int(input("Would you like to play again?  Press 1 to play again! "))
