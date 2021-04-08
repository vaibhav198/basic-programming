"""
Python program to check if a number is prime number or not
"""
import math
#function to check if a number is prime (approach 1)
def Isprime1(a):
	flag = 0
	if a == 2:
		print(f"{a} is even prime number.")
	else:
		for i in range(2, a):
			if a%i == 0:
				flag = 1
				print(f"{a} is not a prime number.")
				break
		if flag == 0:
			print(f"{a} is a prime number.")

#function to check if a number is prime (approach 2)
def Isprime2(a):
	flag = 0
	if a == 2:
		print(f"{a} is even prime number.")
	else:
		for i in range(2, int(math.sqrt(a))):
			if a%i == 0:
				flag =1
				print(f"{a} is not a prime number.")
				break
		if flag == 0:
			print(f"{a} is a prime number.")

#get input from user
num = int(input("Enter a number: "))

print("checking with O(n) time complexity.")
Isprime1(num)

print("Checking with O(sqrt(n)) time complexity.")
Isprime2(num)
