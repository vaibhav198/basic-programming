"""
program to add two numbers
"""

#function that return sum of 2 numbers
def sum2num(num1, num2):
	return num1+num2
#take input from user
num1 = int(input("Enter 1st integer: "))
num2 = int(input("Enter 2nd integer: "))

print(f"Sum of {num1} and {num2} is {sum2num(num1, num2)}")