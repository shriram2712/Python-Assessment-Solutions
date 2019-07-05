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

#Accepting the input from the user
l1 =[]
l2 =[]
n = int(input("Enter the no of pairs"))
for i in range(n):
	for j in range(2):
		name = input("Enter the element ")
		l2.append(name)
	l1.append(set(l2))
	l2.clear()
print ("Pairs are :", l1)


# checking the intersection between two sets while looping through them, if there is an intersection, take the union and delete the other set
l = n
i=0
while i < l-1:
	j = i+1
	while j < l:
		c = l1[i].intersection(l1[j])
		if (not len(c)  == 0):
			d = l1[i].union(l1[j])
			l1[i] = d
			l1.remove(l1[j])
			l = l-1 
		else :
			j = j+1
	i = i+1
	if i == l-1 :
		c = l1[i].intersection(l1[i-1])
		if (not len(c)  == 0):
			d = l1[i].union(l1[i-1])
			l1[i] = d
			l1.remove(l1[i-1])
			l = l-1 


print("THe groups are ", l1)

set1=set()
n1 = input("Enter the relationship to check :\n enter the first name: ")
set1.add(n1)
n2 = input("Enter the second name ")
set1.add(n2)

#Looping through sets and checking if the intersection is 2 then they are related
r = False
for i in l1:
	c = set1.intersection(i)
	if ( len(c) == 2):
		r = True
		break

if r == True:
	print ("Yes, related")
else:
	print ("Not related")









