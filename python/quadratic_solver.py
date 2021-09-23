# Python Program 01 - Calculator (ENGR4)
#Written by Christian Millard
#9.21.2021

from math import sqrt

print("Quadratic Solver")
print("enter the coefficients for ax^2 + bx + c = 0")
print("enter the coefficient a")
a = int(input())
print("enter the coefficient b")
b = int(input())
print("enter the coefficient c")
c = int(input())

d = b ** 2 - 4 * a * c
if(d > 0):
    print("Root #1: ", 
(-b + sqrt(b ** 2 - 4 * a * c))/ 2 * a
)
    print("Root #2: ", (-b - sqrt(b ** 2 - 4 * a * c))/ 2 * a)
if(d == 0):
    print("Root #1: ", 
(-b + sqrt(b ** 2 - 4 * a * c))/ 2 * a
)
if(d < 0):
    print("there are no real roots")
