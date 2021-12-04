import random

myDictionary = ["train", "bus", "electrobike", "informatics", "guess", "idea", "school", "calendar"]

letterList = []
guess = []

word = random.choice(myDictionary)

for letter in word:
    letterList.append(letter)
    guess.append("_")

def guessFunc():
    letterGuess = str(input("What is your guess? "))
    
    if letterGuess in letterList:
        for x in range(len(letterList)):
            if letterList[x] == letterGuess:    
                guess[x] = letterGuess
        print(f'this was correct, {"".join(guess)}')
    else:
        print("This was not correct")

x = 0
while x < len(letterList):
    guessFunc()