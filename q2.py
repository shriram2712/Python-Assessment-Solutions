# Write a program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple. The program should be dynamic enough with the input list of tuples.

# function to return the last element of each tuple
# def last(n):
#     return n[-1]  

# sorted() function using the key which is the last element of each tuple  
def sort(list):
    # return sorted(list, key=last)
    return sorted(list, key = lambda n : n[-1])

# Dynamic input for list of tuples
l1 = []
l2 = []
n = int(input("Enter the number of tuples "))
for i in range(n):
	tl = int(input("Enter the number of Elements in the tuple "))
	for j in range(tl):
		number = int(input("Enter the element "))
		l2.append(number)
	l1.append(tuple(l2))
	l2.clear()

l1 = sort(l1)
print("Sorted List is ", l1)


