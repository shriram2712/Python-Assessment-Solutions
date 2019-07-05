#Python Program for binary search of an element i, in a list

# Write a binary search function which searches for an element in a list. Your output should return the index of element if it is present otherwise raise an exception ‘Element not found’


#User Defined Exception class 
class UsEx(Exception):
	def __init__(self,msg):
		self.msg = msg;

	# Binary Search function
	def binary_search(list , l , r, x):
		# For single element in array 
		if r-l == 1:
			if list[l] == x:
				return mid
			else:
				return -1

		# For Multiple elements	in array	
		if r > l :
			mid =  (l+r-1)//2

			# If element is the middle element 
			if list[mid] == x:
				return mid
			# Search in left half of array if middle element is greater than the search element
			elif list[mid] > x:
				return UsEx.binary_search(list, l ,mid-1 ,x)
			# Search in right half of array if middle element is greater than the search element
			elif list[mid] < x:
				return UsEx.binary_search(list, mid+1 , r ,x)
		else:
			return -1		

l1 = []
n = int(input("Enter the size of the list: "))
for i in range(n):
	l1.append(int(input("Enter the element:")))
l1.sort();
print("The Sorted list is: ", l1)
e = int(input("Enter the element to be searched: "))
try:
    index = UsEx.binary_search(l1, 0, n , e)
    #Raise an exception if element is not found
    if index == -1:
    	raise UsEx("Element not found")
    # Print position of element if found
    else:
    	print("Element found at position : ",index)
except UsEx as ue:
	print("Exception: ", ue.msg)