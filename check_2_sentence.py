#Python program to check if two 
#sentence can be made the same by rearranging the words (considering all the words in lowercase)

#you are given 2 strings s1 and s2, you need to check 
#if the two sentence can be make same by rearranging the words
from collections import Counter

"""Method1 is - split both string, sort the list and then compare both list, 
if lists are same then we can make both string same 
by rearranging words"""

def check_sim1(S1, S2):
	list1 = S1.split()
	list1.sort()
	list2 = S2.split()
	list2.sort()
	if list1 == list2:
		return True
	else:
		return False

"""Method2 split both string and then send the list into Counter() 
and then compare both Counter, if both the Counter is same the strings same"""

def check_sim2(S1, S2):
	list1 = S1.split()
	list2 = S2.split()
	listcounter1 = Counter(list1)
	listcounter2 = Counter(list2)
	if listcounter1 == listcounter2:
		return True
	else:
		return False

#Take inputs from user
s1 = input("Enter your first string: ")
s2 = input("Enter your second string: ")

#Calling 1st method
if check_sim1(s1, s2):
	print("Yes")
else:
	print("No")

#calling second method
if check_sim2(s1,  s2):
	print("Yes")
else:
	print("No")





