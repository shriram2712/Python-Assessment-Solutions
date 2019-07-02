# Given pairs of employees who have worked together in a project, 
# a.	find the total number of group of employees who are connected to each other
# b.	given a pair of employees, find if they are connected to each other

# Example:
# Input:
# Pradnya Anisha
# Austin Pradnya
# Austin Melburne
# Vishal Akash
# Rahul Pavan

# Output:
# a.	3. The three groups are (Pradnya, Anisha, Austin, Melburne) and (Vishal, Akash) and (Pavan, Rahul)
# b.	(Pradnya, Melburne) - Yes
# (Pavan, Vishal) - No

# Python code to find common 
# first element in list of tuple 

# Function to solve the task 
def find(Input): 
	out = {} 
	for elem in Input: 
		try: 
			out[elem[0]].extend(elem[1:]) 
		except KeyError: 
			out[elem[0]] = list(elem) 
	return [tuple(values) for values in out.values()] 

# List initialization 
Input = [('x', 'y'), ('x', 'z'), ('w', 't')] 

# Calling function 
Output = (find(Input)) 

# Printing 
print("Initial list of tuple is :", Input) 
print("List showing common first element", Output) 















# # Python code to find common first 
# # element in list of tuple 

# # Importing 
# from collections import defaultdict 

# # Function to solve the task 
# def find(pairs): 
# 	mapp = defaultdict(list) 
# 	for x, y in pairs: 
# 		mapp[x].append(y) 
# 	return [(x, *y) for x, y in mapp.items()] 

# # Input list initialization 
# Input = [('p', 'q'), ('p', 'r'), 
# 		('p', 's'), ('m', 't')] 

# # calling function 
# Output = find(Input) 

# # Printing 
# print("Initial list of tuple is :", Input) 
# print("List showing common first element", Output) 


