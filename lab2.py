"""""""""""""""""""""
Lab2 - find median
2/22/2019 - Ken M. Amamori
CS2302 MW 10:30 - 11:50
"""""""""""""""""""""
from random import random
import copy
import time

""""""""""""""""""""""""""""""""""""
#List Functions
class List(object):
    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None

class Node(object):
    # Constructor
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""

#return a copy of L
def Copy(L):
	C = List()
	temp = L.head
	while temp is not None: #iterate every node
		Append(C, temp.item) #append each item into C
		temp = temp.next
	return C

#return the item at n of L
def ElementAt(L, n):
	if getLength(L)<n: #base case
		return null
	else:
		temp = L.head
		for i in range(n): #iterate for n times
			temp = temp.next
		return temp.item #return the item at n

#dicide which algorithm to use
def Median(L):
	C = Copy(L) #get the copy of L
	print("Using bubble Sort.\n\tThe median is: ", BubbleSort(C)) #get the median using Bubble Sort
	#print("Using Merge Sort.\n\tThe median is: ", ElementAt(MergeSort(C), getLength(C)//2)) #get the median using Merge Sort`
	#print("Using Quick Sort.\n\tThe median is: ", ElementAt(QuickSort(C), getLength(C)//2)) #get the median using quick sort
	#print("Using Modified Quick Sort.\n\tThe median is: ", MQS(C, getLength(C)//2)) # get median using modified QS
	return

#return the median after sorting the list in ascending order using modified quick sort
def MQS(L, n):
	global count
	p = L.head.item #pivot
	SmallL = List() #list for smaller numbers
	LargeL = List() #list for larger numbers
	temp = L.head.next
	while temp is not None: #go through each node
		if temp.item < p: #smaller than pivot
			count+=1
			Append(SmallL, temp.item)
		else: #equal or greater than pivot
			count+=1
			Append(LargeL, temp.item)
		temp = temp.next

	if getLength(SmallL)<n: #median not in smallL
		count+=1
		return MQS(LargeL, n-getLength(SmallL)-1) #search on LargeL and get right the index for median
	elif getLength(SmallL)>n: #median not in LargeL
		count+=1
		return MQS(SmallL, n) #search on SmallL and get the right index for median
	else:
		return p #median

#return the sorted list
def QuickSort(L):
	global count
	if getLength(L)<=1: #base case
		return L
	p = L.head.item #pivot
	SmallL = List() #list for smaller numbers
	LargeL = List() #list for larger numbers
	temp = L.head.next #get the next node
	while temp is not None: #iterate every node
		if temp.item < p: #smaller than pivot
			count+=1
			Append(SmallL, temp.item)
		else: #greater or equal to pivot
			count+=1
			Append(LargeL, temp.item)
		temp = temp.next

	SL = List() #Smaller numbers List
	SL = QuickSort(SmallL) #recursive call
	LL = List() #larger numbers list
	LL = QuickSort(LargeL) #recursive call

	newL = List() #new list which will be combined
	if IsEmpty(SL): #if pivot is the smallest number
		Append(newL, p)
		newL.head.next = LL.head
		newL.tail = LL.tail
		return newL
	elif IsEmpty(LL): #if pivot is the largest number
		Append(SL, p)
		return SL
	else: #pivot in middle
		Append(SL, p)
		SL.tail.next = LL.head
		SL.tail = LL.tail
		return SL

#return the length of L
def getLength(L):
	temp = L.head
	c = 0 #counter
	while temp is not None: #iterate every node
		c+=1
		temp = temp.next
	return c #return the length

#merge sort: sort the list in ascending order and return the list
def MergeSort(L):
	global count
	len = getLength(L) #get the length of L
	if len <= 1: #base case
		return L
	leftL = List() #create a list for left side
	rightL = List() #create a list for right side
	temp = Copy(L) #get the copy of L

	c=0
	#separete the list in two
	for i in range(len//2): #itetrate the list up to len/2
		Append(leftL, temp.head.item) #append current item into leftL
		temp.head = temp.head.next
		c+=1
	while c < len: #iterate the rest of the list
		Append(rightL, temp.head.item) #append current item into rightL
		temp.head = temp.head.next
		c+=1

	LL = List() #LeftList
	LL = MergeSort(leftL) #recursive call for the left side of the list
	RL = List() #RightList
	RL = MergeSort(rightL) #recursive call for right side

	TL = List() #Total List

	while getLength(TL)!=len: #keep iterating until TL has all items
		if IsEmpty(RL): #Right list empty
			Append(TL, LL.head.item)
			LL.head = LL.head.next
		elif IsEmpty(LL): #Right list empty
			Append(TL, RL.head.item)
			RL.head = RL.head.next
		elif RL.head.item < LL.head.item: #when RL item is smaller than LL item
			count+=1
			Append(TL, RL.head.item)
			RL.head = RL.head.next
		else: #when LL item is smaller than RL item
			count+=1
			Append(TL, LL.head.item)
			LL.head = LL.head.next
	return TL #return the merged list

#sort the list in ascending order using bubble sort and return the median
def BubbleSort(L):
	c=True
	global count
	while c: #checks if there was any swap in previus iteration
		temp = L.head
		while temp.next is not None: #traverse every nodes except the last one
			if temp.item > temp.next.item: #true then swap
				count = count+1
				tnum = temp.item
				temp.item = temp.next.item
				temp.next.item = tnum
				c=False
			temp = temp.next #get the next node
		c = not c #get the inverse to see if there is any need to continue checking the list
	return ElementAt(L, getLength(L)//2) #return the median

def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line

def IsEmpty(L):
    return L.head == None

def Append(L,x):
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next

# generate a list of length n with random numbers
def createList(L, n):
	for i in range(n):
		Append(L, int(random()*101)) #append a number between 0 and 100 into L

count = 0 #global variable in order to keep track of comparison
n = int(input("Enter the length of the list.")) #input from the user
L = List() #creating a list
createList(L, n) #create a list of length n
print("List: \t", end='')
Print(L) #print the original list
start = int(time.time()*1000) #starting time
Median(L) #get the median of the list (L)
end = int(time.time()*1000) #ending time
print(count, "comparison") #num of total comparison
print(end-start , "seconds.") #resutl time
