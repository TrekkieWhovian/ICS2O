enterAgain = "yes"
while(enterAgain != "no"):
    word1 = str(input("Enter a word: "))
    word2 = str(input("Enter a word: "))
    word3 = str(input("Enter a word: "))
    word1 = word1.lower()
    word2 = word2.lower()
    word3 = word3.lower()
    if(word1 < word2 < word3):
        print("The words in order are:", word1+",", word2+",", word3)
    elif(word1 < word3 < word2):
        print("The words in order are:", word1+",", word3+",", word2)
    elif(word2 < word1 < word3):
        print("The words in order are:", word2+",", word1+",", word3)
    elif(word2 < word3 < word1):
        print("The words in order are:", word2+",", word3+",", word1)
    elif(word3 < word1 < word2):
        print("The words in order are:", word3+",", word1+",", word2)
    else:
        print("The words in order are:", word3+",", word2+",", word1)
    enterAgain = str(input("Enter again? "))
print("Goodbye")
