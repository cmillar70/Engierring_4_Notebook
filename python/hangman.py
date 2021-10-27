# Python Program 06 - Man Shaped Pinata (ENGR4)
#Written by Christian Millard
#9.28.2021

import sys #so we can exit the program with a command later

def man(bWrong): #This is a function I made to easily call the small text art of a man 
    if bWrong == 0:
        print("""
|---┐ 
            """)
    if bWrong == 1:
        print("""
|---┐ 
    0
            """)
    if bWrong == 2:
        print("""
|---┐ 
    0
    |
            """)
    if bWrong == 3:
        print("""
|---┐ 
    0
   \|
            """)
    if bWrong == 4:
        print("""
|---┐ 
    0
   \|/
            """)
    if bWrong == 5:
        print("""
|---┐ 
    0
   \|/
    |
            """)
    if bWrong == 6:
        print("""
|---┐ 
    0
   \|/
    |
   /
            """)
    if bWrong == 7:
        print("""
|---┐ 
    0
   \|/
    |
   / \
            """)

print("Player 1, enter your word:")
cWord = input() #this records the first input as the word we will be guessing
print("\n"*50) #clearing the screen so player 2 can't see it
blanks = "_" * len(cWord) #making the blanks the length of the word
jCorrect ="" #the letters you have correctly guessed
kMisses ="" #the letters you have incorrectly guessed
bWrong = 0 #number of wrong letters you've guessing
iRight = 0 #number of correct letters you've guessed
eLetters = list(cWord) #splitting the word into letters
fMissPhrase = "Missed Letters:" #saving these two phrases so I don't have to write them out every time
gGuessPhrase = "Guess a Letter:"
while True: #this while loop check if you have won yet after every guess and ends the game if you have 
    print("\n" * 50) #clears the screen at the beginning of every turn
    if blanks == cWord:
        print("the word was: ", cWord, "\n")
        print("You win!")
        sys.exit()
    else:
        man(bWrong)
        print(fMissPhrase, kMisses, "\n")
        print(blanks, "\n")
        print(gGuessPhrase)
        hGuess = input()
        if hGuess in eLetters:
            iRight = iRight + 1
            jCorrect = jCorrect + hGuess
        
        else:
            bWrong = bWrong + 1
            kMisses = kMisses + hGuess
    for i in range(len(cWord)):
        if cWord[i] in jCorrect:
            blanks = blanks[:i] + cWord[i] + blanks[i+1:]
