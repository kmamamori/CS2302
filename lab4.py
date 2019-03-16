"""""""""""""""""""""
Lab 4 - B-trees
03/15/2019 - Ken M. Amamori
CS2302 MW 10:30 - 11:50
Professor: Olac Fuentes
TA: Anindita Nath, Maliheh Zargaran
"""""""""""""""""""""

import math

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):
        self.item = item
        self.child = child
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items


#find the depth at which it is found in the tree
def findDepthOfk(T, k):
	d = 0
	if T.isLeaf:
		if k in T.item: #T.item contians k
			return 0
		else:
			return -1
	if k <= T.item[-1]: #k is less than the last element
		for i in range(len(T.item)): #compare with each elements
			if k==T.item[i]: #equal
				return 0
			if k<T.item[i]: #k is less
				d = findDepthOfk(T.child[i], k) #call with appropriate T node
				break #break the loop
	else:
		d = findDepthOfk(T.child[-1], k) #call with last child
	if d == -1: #not found case
		return -1
	else:
		return d + 1

#find the number of leaves in the tree that are full
def FullLeaves(T):
	if T.isLeaf and len(T.item)==T.max_items: #len(T.item)=max_item
		return 1
	d = 0
	for i in range(len(T.child)): #traverse through childs
		d += FullLeaves(T.child[i])
	return d #return value

#find the number of nodes in the tree that are full
def countFullNode(T):
	if T.isLeaf: #
		if len(T.item) == T.max_items: #T is full
			return 1
		else:
			return 0
	else:
		d = 0
		for i in range(len(T.child)): #traverse through each element
			d += countFullNode(T.child[i])
		if len(T.item) == T.max_items: #checks if it is full
			return 1 + d
		else:
			return d

#print all the items in the tree at a given depth d
def printAtDepth(T, d):
	if T.isLeaf and d!=0: #d>height
		return
	if d==0: #depth wanted
		for i in T.item: #travese through each elements
			print(i, " ", end='')
	else:
		for i in range(0, len(T.child), 1):
			printAtDepth(T.child[i], d-1) #call evert childs

#find the number of nodes in the tree at a given depth d
def nodesAtDepth(T, d):
	if T.isLeaf and d!=0:
		return 0 #d>height
	if d==0:
		return 1 #exit one node
	k = 0
	for i in range(len(T.child)): #traverse each child
		k += nodesAtDepth(T.child[i], d-1) #add number of elemnts to k
	return k #return the value

#find the maximum element in the tree at given depth d
def maxAtDepth(T, d):
	if T.isLeaf and d!=0: #is leaf and not d=0
		return -math.inf
	if d==0: #depth wanted
		return T.item[-1] #return max element
	return maxAtDepth(T.child[-1], d-1)

#find the minimum element in the tree at a given depth d
def minAtDepth(T, d):
	if T.isLeaf and d!=0: #is leaf but not at d=0
		return math.inf
	if d==0: #depth wanted
		return T.item[0] #return min element
	return minAtDepth(T.child[0], d-1)

#extract the items in the B-tree into a sorted list
def extract_tree(T):
	if T is not None: #not null
		if T.isLeaf:
			return T.item
		d = []
		for i in range(len(T.item)): #traverse through child[0:-2]
			d += extract_tree(T.child[i]) + [T.item[i]]
		d += extract_tree(T.child[-1]) #add the last child
		return d

#find the height of the tree
def height(T):
	if T.isLeaf:
		return 0
	return 1 + height(T.child[0])

"""Uploaded by Prof. Fuentes"""
def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)

def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m)
            T.child[k] = l
            T.child.insert(k+1,r)
            k = FindChild(T,i)
        InsertInternal(T.child[k],i)

def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid])
        rightChild = BTree(T.item[mid+1:])
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf)
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf)
    return T.item[mid], leftChild,  rightChild

def InsertLeaf(T,i):
    T.item.append(i)
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)
        InsertInternal(T.child[k],i)

def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
"""Uploaded by Prof. Fuentes"""

L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5, 105, 115, 200, 2, 45, 6, 9, 81, 82, 83, 84, 85, 123, 134, 136, 156, 245, 346, 456, 56, 456, 343, 444, 555, 666, 777, 888, 999, 232, 544, 542, 657, 325, 958, 546, 657, 876, 674]
T = BTree()
for i in L:
    print('Inserting',i)
    Insert(T,i)
    PrintD(T,'')
    #Print(T)
    print('\n####################################')

print("The height of the tree:", height(T)) #part1#
print("List extracted from the tree:", extract_tree(T)) #part2#
d = 2 #depth
print("Min value at depth",d,"is:", minAtDepth(T, d)) #part3#
print("Max value at depth",d,"is:", maxAtDepth(T, d)) #part4#
print("Total nodes at depth", d,"is:", nodesAtDepth(T, d)) #part5#
printAtDepth(T, 2) #part6#
print(0)
print("There is/are", countFullNode(T), "full nodes in the tree.") #part7#
print("There is/are", FullLeaves(T), "full nodes at leaf in the tree.") #part8#
k = 30 #key number
print("The number",k, "is at depth:", findDepthOfk(T, k),end='.') #part9#
