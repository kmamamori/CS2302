"""""""""""""""""""""
Lab 3 - Binary Search Trees
03/08/2019 - Ken M. Amamori
CS2302 MW 10:30 - 11:50
"""""""""""""""""""""

import matplotlib.pyplot as plt

""""""""""""
class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
""""""""""""""""""

#find the height of a tree
def find_height(T):
	if T is not None: #base case
		return (1+max([(find_height(T.left)), find_height(T.right)])) #1 + (the higher number)
	else:
		return -1

#print elements at depth k
def printAtdepth(T, k):
	if T is None: # base case
		return
	if k==0: #reached the depth
		print(T.item, " ", end='')
	else:
		printAtdepth(T.left, k-1) #recursive call for left child
		printAtdepth(T.right, k-1) #recursive call for right child

#print each depth and stops when counter reaches the height of the tree
def print_depthorder(T, k, h):
	if h != k: #base case
		print("Keys at depth",k,":  ", end='')
		printAtdepth(T, k) #call a method which prints items
		print()
		print_depthorder(T, k+1, h) #recursive call, add one to k

#Extract elements in a tree into sorted array
def extract_tree(T):
	if T is not None: #base case
		if T.left is None: #reached the last element
			return [T.item] #return the current number
		if T.right is not None: #both left and right child exist
			return extract_tree(T.left) + [T.item] + extract_tree(T.right) #recursive call: left,node,right (infix)
		else: #no right child
			return extract_tree(T.left) + [T.item]

#build a balanced binary search tree with given sorted list A
def balanced_tree(T, A):
	l = len(A) #get the length of the tree
	if l>0: #base case
		l = l//2 #get the middle number
		T = BST(A[l]) #insert number
		T.left = balanced_tree(T.left, A[:l]) #recursive call for left child with new array
		T.right = balanced_tree(T.right, A[l+1:]) #recursive call for right child with new array
	return T

#print item if T is not None, "no such item" when None node
def print_node(T):
	if T is not None:
		return T.item
	else:
		return "no such item"

#search a number k in the tree T, return node with the same number if it was found, None if not found
def search_num(T, k):
	temp = T #temporary variable for T
	while temp is not None: #iterate through necessary nodes
		if temp.item > k: #the number is smaller
			temp = temp.left
		elif temp.item < k: #the number is larger
			temp = temp.right
		else: #current item == k
			return temp #return node with the same number as k
	return None #not found

#draw a tree with numbers
def draw_tree(ax, c, T, dx, dy):
	if T.left is not None: #checks if left child exist
		ax.plot([c[0], c[0]-dx], [c[1], c[1]-dy], color='k') #draw a line towards left child
		draw_tree(ax, [c[0]-dx, c[1]-dy], T.left, dx*0.5, dy*0.9) #recursive call with new root
	if T.right is not None: #checks if right child exist
		ax.plot([c[0], c[0]+dx], [c[1], c[1]-dy], color='k') #draw a line towards right child
		draw_tree(ax, [c[0]+dx, c[1]-dy], T.right, dx*0.5, dy*0.9) #recursive call with new root
	plt.plot(c[0], c[1], 'wo', markersize=23, markeredgecolor='black') #draw a white circle at 'c' with size of 23 and black edge color
	ax.annotate(T.item, [c[0]-2.5, c[1]-2]) #plot a number inside of a circle

#insert a number into binary search tree
def Insert(T, newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left, newItem)
    else:
        T.right = Insert(T.right, newItem)
    return T

#print a tree in inorder
def InOrder(T, space):
	if T is not None:
		InOrder(T.left, space+'	')
		print(space, T.item)
		InOrder(T.right, space+'	')

T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100]
for a in A:
    T = Insert(T,a)
InOrder(T, '	')

"""Part-2"""
print("There is", print_node(search_num(T, 130)), "in the tree.")

"""Part-3"""
T1 = None
A1 = [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 15, 18]
T1 = balanced_tree(T1, A1)

"""Part-4"""
print("Extract tree into an array:", extract_tree(T1))

"""Part-5"""
print_depthorder(T1, 0, find_height(T1)+1)

"""Part-1"""
plt.close("All")
fig, ax = plt.subplots()
draw_tree(ax, [0,0], T1, 50, 50) #ax, center, tree, dx, dy
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
