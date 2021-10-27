# Python Program 04 - Quadratic Calculator (ENGR4)
#Written by Christian Millard
#9.20.2021

from math import sqrt #regular python can't do square roots so we need to import that command

print("Quadratic Solver") #title
print("enter the coefficients for ax^2 + bx + c = 0") # enter the 3 coefficients
print("enter the coefficient a")
a = int(input()) 
print("enter the coefficient b")
b = int(input())
print("enter the coefficient c")
c = int(input())

d = b ** 2 - 4 * a * c #d stands for 'discriminant", a section of the quadratic formula that tells us how many real roots we have
if(d > 0): #if we get higher than 0 there are 2 real roots
    print("Root #1: ", (-b + sqrt(b ** 2 - 4 * a * c))/ 2 * a) #calculate the first root
    print("Root #2: ", (-b - sqrt(b ** 2 - 4 * a * c))/ 2 * a) #calculate the second root
if(d == 0): # if we get 0 there is 1 real root
    print("Root #1: ", (-b + sqrt(b ** 2 - 4 * a * c))/ 2 * a) #calculate the root
if(d < 0): #if we get less than 0 there are no real roots
    print("there are no real roots")
