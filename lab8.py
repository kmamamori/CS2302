"""""""""""""""""""""""""""""""""""""""
Lab 8 - Algorithm Design Techniques
05/09/2019 - Ken M. Amamori
CS2302 MW 10:30 - 11:50
Professor: Olac Fuentes
TA: Anindita Nath, Maliheh Zargaran
IA: Eduardo Lara	PL: Erick Macik
"""""""""""""""""""""""""""""""""""""""
import random
from mpmath import *
import numpy as np

#randamization part, tries 1000 times and verify if they are same
def equal(f1, f2,tries=1000,tolerance=0.0001):
	for i in range(tries):
		x = random.random() #get random number
		y1 = eval(f1)
		y2 = eval(f2)
		if np.abs(y1-y2)>tolerance: #compare if there is any difference
			return False
	return True

#make every possible pair and send to "equal" to verify it
def checkeq(eq):
	for i in range(len(eq)):
		for j in range(i+1, len(eq), 1):
			if equal(eq[i], eq[j]): #test with randomization
				print(eq[i], "&", eq[j], "are the same.")

#find if there is any subset that meet the criterial by backtracking
def findsubset(S, S2, last, g):
	if g==0: #found
		return True, []
	if g<0 or last<0: #not found
		return False, []
	res, subset = findsubset(S, S2, last-1, g-S[last])
	if res:
		subset.append(S[last]) #add because it is part of the first subset
		S2.remove(S[last]) #remove because it is part of the other subset
		return True, subset
	else:
		return findsubset(S, S2, last-1, g) #do not add the last element

def partition(S):
	t = sum(S)
	if t%2==0:
		S2=[i for i in S] #copy S
		a, s = findsubset(S, S2, len(S)-1, t//2) #check if there is a subsets that are equal
		if a: #found
			print("\nMain set:", S)
			print("Solution:", s, " & ", S2)
		else: #not found
			print("There is no solution")
	else: #no solution
		print("There is no solution")

#part 1
eq = ['sin(x)', 'cos(x)', 'tan(x)', 'sec(x)', '-sin(x)', '-cos(x)', '-tan(x)', '-sin(x)', 'cos(-x)', 'tan(x)', 'sin(x)/cos(x)', '2*sin(x/2)*cos(x/2)', 'sin(x)*sin(x)', '1-cos(x)*cos(x)', '((1-cos(2*x))/2)', '1/cos(x)']
checkeq(eq)

#part 2
S = [1, 2, 4, 6, 9, 12] #parent set
partition(S)
