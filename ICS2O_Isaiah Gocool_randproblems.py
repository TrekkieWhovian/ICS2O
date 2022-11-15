#Isaiah Gocool
#ICS2O
#February 22, 2019
#Randomly generates a math problem and asks the user for the answer
import random
num1 = int(random.randint(-5, 8))
num2 = int(random.randint(-5, 8))
num3 = int(random.randint(-5, 8))
num4 = int(random.randint(-5, 8))
num5 = int(random.randint(-5, 8))
num6 = int(random.randint(-5, 8))
num7 = int(random.randint(-5, 8))
num8 = int(random.randint(0, 3))
num9 = int(random.randint(-5, 8))
num10 = int(random.randint(-5, 8))
num11 = int(random.randint(-5, 8))
num12 = int(random.randint(-5, 8))
num13 = int(random.randint(-5, 8))
num14 = int(random.randint(-5, 8))
print("Problem 1:" , num1 , "+" , num2)
print("Problem 2:" , num3 , "-" , num4)
print("Problem 3:" , num5 , "*" , num6)
print("Problem 4:" , num7 , "**" , num8)
print("Problem 5:" , num9 , "/" , num10)
print("Problem 6:" , num11 , "//" , num12)
print("Problem 7:" , num13 , "%" , num14)
sol1 = int(input("What is the solution to the first problem? "))
if sol1 == (num1 + num2):
    print("You have the correct answer")
else:
    print("You have the wrong answer")
sol2 = int(input("What is the solution to the second problem? "))
if sol2 == (num3 - num4):
    print("You have the correct answer")
else:
    print("You have the wrong answer")
sol3 = int(input("What is the solution to the third problem? "))
if sol3 == (num5 * num6):
    print("You have the correct answer")
else:
    print("You have the wrong answer")
sol4 = int(input("What is the solution to the fourth problem? "))
if sol4 == (num7 ** num8):
    print("You have the right answer")
else:
    print("You have the wrong answer")
sol5 = float(input("What is the solution to the fifth problem? "))
if sol5 == (num9 / num10):
    print("You have the correct answer")
else:
    print("You have the wrong answer")
sol6 = int(input("What is the solution to the sixth problem? "))
if sol6 == (num11 // num12):
    print("You have the right answer")
else:
    print("You have the wrong answer")
sol7 = int(input("What is the solution to the seventh problem? "))
if sol7 == (num13 % num14):
    print("You have the right answer")
else:
    print("You have the wrong answer")
