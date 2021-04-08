"""
Python program to check if a given number is even of odd
"""

#Function to check even/odd number
def Check_EvenOdd(a):
	if a%2 == 0:
		print(f"{a} is even.")
	else:
		print(f"{a} is odd.")

#get input from user
num = int(input("Enter a number: "))

Check_EvenOdd(num)