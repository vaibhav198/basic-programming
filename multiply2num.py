"""
program to multiply two numbers
"""

#function that returns multiplication of two numbers
def multi2num(num1, num2):
	return num1*num2

#take input from user
num1 = int(input("Enter 1st integer: "))
num2 = int(input("Enter 2nd integer: "))

print(f"Multiplication of {num1} and {num2} is {multi2num(num1, num2)}")