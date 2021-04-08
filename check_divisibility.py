"""
Python program to check if a is divisible by b.
"""

#function to check divisibility
def Check_divisibility(a, b):
	if a%b == 0:
		return True
	else:
		return False

#Take input from user
num1, num2 = map(int, input("Enter two number (space separated): ").strip().split())

if Check_divisibility(num1, num2):
	print(f"{num1} is divisible by {num2}")
else:
	print(f"{num1} is not divisible by {num2}")