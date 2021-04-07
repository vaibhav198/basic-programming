"""
program to find out division between two number
"""

#function to find division
def division2num(num1, num2):
	return num1/num2

#function to calculate modulo
def modulo2num(num1, num2):
	return num1%num2
	
#take input from user
num1 = int(input("Enter 1st integer: "))
num2 = int(input("ENter 2nd integer: "))

if num2 != 0:
	print(f"Division of {num1} and {num2} is {division2num(num1, num2)}")
else:
	print("Division not defined, because denominator is Zero.")

if num2 != 0:
	print(f"Modulous of {num1} with {num2} is {modulo2num(num1, num2)}")
else:
	print("Modulo not defined, because denominator is Zero.")