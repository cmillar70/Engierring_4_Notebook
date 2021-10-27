# Python Program 05 - Strings and Loops (ENGR4)
#Written by Christian Millard
#9.21.2021

print("type your text, then press enter: ")
x = input() #the phrase you input
y = x.split(" ") #splits the phrase into a list of words
for z in y: #counts the number of words in the phrase
    for a in z: #counts the number of letters in each word
        print(a) # prints the next letter
    print("-") #puts a dash between words
