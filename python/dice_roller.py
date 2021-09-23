# Python Program 02 - Dice Roller (ENGR4)
#Written by Christian Millard
#9.14.2021
input("press enter to roll")
from random import randint
print ("Automatic Dice Roller")
print ("The value is:")
print (randint(1,6))
rol = input("roll again?")
while rol == "":
    print ("The value is:")
    print (randint(1,6))
    rol = input("roll again?")
