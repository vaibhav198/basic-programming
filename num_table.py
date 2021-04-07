"""
program to get table of a number
"""

#function to get table of a number
def Num_table(num):
	return [i*num for i in range(1, 11)]

#get the input from user
while(True):
	print("Choose an option:-")
	print("1 : to enter an Integer.")
	print("2 : to exit (you can choose any other number except 1).")
	option = int(input())
	if option == 1:
		num = int(input("Enter an Integer: "))
		print(f"Table of {num} is \n{Num_table(num)}")
	else:
		break

