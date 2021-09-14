# Automatic Dice Roller
# Written by Christian
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
