#Isaiah Gocool
#ICS2O
#February 26, 2019
#Generates two random numbers and provides a message to the user depending on the sum
import random
num1 = int(random.randint(1, 6))
num2 = int(random.randint(1, 6))
exponent = (num1**num2)
name = input("What is your name? ")
print("The random numbers are" , num1 , "and" , num2)
sum = (num1 + num2)
if sum < 8 and sum > 6:
    print("Common Result")#Prints "Common Result" if the sum is between 6 and 8
elif sum < 5:
    print("The sum is" , sum)
    print("Small sum")#Prints the sum and "Small sum" if the sum is less than 5
    if num2 < 2:
        print(num1 , "^" , num2 , "=" , exponent)#Prints the result of raising num1 to the exponent of num2 if num2 is less than 2
else:#Prints two random numbers if the sum is not any of the above scenarios
    print(random.randint(num1, num2))
    print(random.randint(num1, num2))
1 = print("Goodbye," , name)
2 = print("Have a good day," , name)
3 = print("See ya," , name)
print(random.randint(1, 3))
