secretWord = "Hidden figures"

guessWord = input("Enter guess word: ")
noOfTries = 0

while guessWord != secretWord and noOfTries < 3:
    print("Failed, try again")
    guessWord = input("Enter guess word: ")
    noOfTries += 1

if noOfTries == 3:
    print("Failed, you exhasted no of tries")

else:
    print("You win")