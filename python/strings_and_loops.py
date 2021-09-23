# Python Program 05 - Strings and Loops (ENGR4)
#Written by Christian Millard
#9.21.2021

print("type your text, then press enter: ")
x = input()
y = x.split(" ")
for z in y:
    for a in z:
        print(a)
    print("-")    
