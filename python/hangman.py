# Python Program 06 - Man Shaped Pinata (ENGR4)
#Written by Christian Millard
#9.28.2021

import sys

def man(bWrong):
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
cWord = input()
print("\n"*50)
blanks = "_" * len(cWord)
jCorrect =""
kMisses =""
bWrong = 0
iRight = 0
eLetters = list(cWord)
fMissPhrase = "Missed Letters:"
gGuessPhrase = "Guess a Letter:"
while True:
    print("\n" * 50)
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
