"""
python program to mask a list using values from another list
"""
"""
Given 2 list, the task is to write a python program that marks 1 for the elements present in the other list else mark 0.
Input1: test_list e.g. [3,5,2,1]
Input2: reference_list [10, 20, 3, 4, 1]
Output: [1,0,0,1]
"""

test_list = list(map(int, input("Enter test list elements (space separated): ").strip().split()))

reference_list = list(map(int, input("Enter reference list elements (space separated): ").strip().split()))

#function that will return masked list
def Mask_list(test_list, reference_list):
	return [1 if ele in reference_list else 0 for ele in test_list]

#calling function

print(f"Masked list is {Mask_list(test_list, reference_list)}")
