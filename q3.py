# Given a new lexicographical order of alphabets, sort the list of strings according to the new order. 
# Example:
# New lexicographical order - [‘r’ , ‘c’, ‘t’ , ‘a’]
# Input list of strings - [‘car’, ‘rat’, ‘cat’]
# Output sorted list - [‘rat’, ‘car’, ‘cat’]


def sort(order, ip): 
      
    # Sort the array according to the new lexicographical order 
    # function which sorts the words according to the respective index from order list
    op = sorted(ip, key = lambda w: [order.index(c) for c in w]) 
    return op
  
order=[]
ip=[]
op=[]
ol = int(input("Enter the length of the lexicographical order "))
for i in range(ol):
	ch = input("Enter the character ")
	order.append(ch)
il = int(input("Enter the length of the input string list "))
for i in range(il):
	ch = input("Enter the string ")
	ip.append(ch)

op = sort(order, ip) 
print(op)
