# Python Program 03 - Calculator (ENGR4)
#Written by Christian Millard
#9.16.2021

def doMath(a,b,c): #a function that allows us to do multiple kinds of math depending on which one you call for
    if c == 1: #if c is 1 do addition
        return str(a + b)
    if c == 2: #if c is 2 do subtraction
        return str(a - b)
    if c == 3: #if c is 3 do multiplication
        return str(a * b)
    if c == 4: #if c is 4 do division
        return str(a / b)
    if c == 5: #if c is 5 show the remainder from division
        return str(a % b)
    
print("enter your first number: ")
a = int(input()) #the first number you want to calculate
print("enter your second number: ")
b = int(input()) #the second number


#calling every part of the function to list all kinds of calculations
print("Sum:\t\t" + doMath(a,b,1))
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))
