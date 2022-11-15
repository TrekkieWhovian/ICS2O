fruits = ["apple", "pear", "peach"]
number = 0
while(number != len(fruits)):
    capFirst = fruits[number][0].upper()
    endWord = (fruits[number][1:len(fruits[number])])
    fruits[number] = (capFirst + endWord)
    number = (number + 1)
vegetable1 = str(input("Enter the first vegetable: "))
vegetable2 = str(input("Enter the second vegetable: "))
vegetable3 = str(input("Enter the third vegetable: "))
veggies = [vegetable1, vegetable2, vegetable3]
food = [fruits[0], fruits[1], fruits[2], vegetable1, vegetable2, vegetable3]
fruits[0] = fruits[0].replace("A", "-")
fruits[0] = fruits[0].replace("a", "-")
fruits[0] = fruits[0].replace("e", "-")
fruits[0] = fruits[0].replace("i", "-")
fruits[0] = fruits[0].replace("o", "-")
fruits[0] = fruits[0].replace("u", "-")
food = [fruits[0], fruits[1], fruits[2], vegetable1, vegetable2, vegetable3]
food.remove(fruits[1])
food.remove(fruits[2])
if(vegetable1[0] == "B" or vegetable1[0] == "b" or vegetable1[0] == "C" or vegetable1[0] == "c" or vegetable1[0] == "D" or vegetable1[0] == "d" or vegetable1[0] == "F" or vegetable1[0] == "f" or vegetable1[0] == "G" or vegetable1[0] == "g" or vegetable1[0] == "H" or vegetable1[0] == "h" or vegetable1[0] == "J" or vegetable1[0] == "j" or vegetable1[0] == "K" or vegetable1[0] == "k" or vegetable1[0] == "L" or vegetable1[0] == "l" or vegetable1[0] == "M" or vegetable1[0] == "m" or vegetable1[0] == "N" or vegetable1[0] == "n" or vegetable1[0] == "P" or vegetable1[0] == "p" or vegetable1[0] == "Q" or vegetable1[0] == "q" or vegetable1[0] == "R" or vegetable1[0] == "r" or vegetable1[0] == "S" or vegetable1[0] == "s" or vegetable1[0] == "T" or vegetable1[0] == "t" or vegetable1[0] == "V" or vegetable1[0] == "v" or vegetable1[0] == "X" or vegetable1[0] == "x" or vegetable1[0] == "Z" or vegetable1[0] == "z" or vegetable1[0] == "W" or vegetable1[0] == "w" or vegetable1[0] == "Y" or vegetable1[0] == "y"):
    food.remove(vegetable1)
if(vegetable2[0] == "B" or vegetable2[0] == "b" or vegetable2[0] == "C" or vegetable2[0] == "c" or vegetable2[0] == "D" or vegetable2[0] == "d" or vegetable2[0] == "F" or vegetable2[0] == "f" or vegetable2[0] == "G" or vegetable2[0] == "g" or vegetable2[0] == "H" or vegetable2[0] == "h" or vegetable2[0] == "J" or vegetable2[0] == "j" or vegetable2[0] == "K" or vegetable2[0] == "k" or vegetable2[0] == "L" or vegetable2[0] == "l" or vegetable2[0] == "M" or vegetable2[0] == "m" or vegetable2[0] == "N" or vegetable2[0] == "n" or vegetable2[0] == "P" or vegetable2[0] == "p" or vegetable2[0] == "Q" or vegetable2[0] == "q" or vegetable2[0] == "R" or vegetable2[0] == "r" or vegetable2[0] == "S" or vegetable2[0] == "s" or vegetable2[0] == "T" or vegetable2[0] == "t" or vegetable2[0] == "V" or vegetable2[0] == "v" or vegetable2[0] == "X" or vegetable2[0] == "x" or vegetable2[0] == "Z" or vegetable2[0] == "z" or vegetable2[0] == "W" or vegetable2[0] == "w" or vegetable2[0] == "Y" or vegetable2[0] == "y"):
    food.remove(vegetable2)
if(vegetable3[0] == "B" or vegetable3[0] == "b" or vegetable3[0] == "C" or vegetable3[0] == "c" or vegetable3[0] == "D" or vegetable3[0] == "d" or vegetable3[0] == "F" or vegetable3[0] == "f" or vegetable3[0] == "G" or vegetable3[0] == "g" or vegetable3[0] == "H" or vegetable3[0] == "h" or vegetable3[0] == "J" or vegetable3[0] == "j" or vegetable3[0] == "K" or vegetable3[0] == "k" or vegetable3[0] == "L" or vegetable3[0] == "l" or vegetable3[0] == "M" or vegetable3[0] == "m" or vegetable3[0] == "N" or vegetable3[0] == "n" or vegetable3[0] == "P" or vegetable3[0] == "p" or vegetable3[0] == "Q" or vegetable3[0] == "q" or vegetable3[0] == "R" or vegetable3[0] == "r" or vegetable3[0] == "S" or vegetable3[0] == "s" or vegetable3[0] == "T" or vegetable3[0] == "t" or vegetable3[0] == "V" or vegetable3[0] == "v" or vegetable3[0] == "X" or vegetable3[0] == "x" or vegetable3[0] == "Z" or vegetable3[0] == "z" or vegetable3[0] == "W" or vegetable3[0] == "w" or vegetable3[0] == "Y" or vegetable3[0] == "y"):
    food.remove(vegetable3)
print(food)
