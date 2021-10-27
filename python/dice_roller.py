# Python Program 02 - Dice Roller (ENGR4)
#Written by Christian Millard
#9.14.2021
input("press enter to roll") #kind of self explanitory
from random import randint #allows us to generate a random number
print ("Automatic Dice Roller") #title
print ("The value is:") 
print (randint(1,6)) #generates a random number between 1 and 6
rol = input("roll again?") #asks if you want to roll again
while rol == "": #while you continue to roll it will continue to loop
    print ("The value is:") #this is all just looping what you saw earlier until you end the program
    print (randint(1,6))
    rol = input("roll again?")
