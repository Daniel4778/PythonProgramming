"""
 Programmer : Paddock
 Program: Function to compute the average of three numbers
 Created on :
 Last Changed :
 Version : Python 3.10
"""

def average(a, b, c):   #function definiton for average calculation
    avg = (a+b+c)/3
    return avg

print("Program to calculate average of three numbers")
a=float(input("Enter the value of a: \t"))
b=float(input("Enter the value of b: \t"))
c=float(input("Enter the value of c: \t"))
result = average(a, b, c)   #calling the average function
print("Average of given numbers\t", result)
