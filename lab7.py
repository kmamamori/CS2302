"""""""""""""""""""""""""""""""""""""""
Lab 7 - Graphs
04/29/2019 - Ken M. Amamori
CS2302 MW 10:30 - 11:50
Professor: Olac Fuentes
TA: Anindita Nath, Maliheh Zargaran
IA: Eduardo Lara	PL: Erick Macik
"""""""""""""""""""""""""""""""""""""""
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import interpolate
import time
import sys
import math
import queue

#print the path from top right corner to 0
def printPath(prev, v):
	if prev[v]!=-1:
		printPath(prev, prev[v])
		print("-", end='')
		print(v, end='')

#solving the maze using DFS rec
def DFS_rec(g, s):
	global visited_rec #global var
	global prev_rec #global var
	visited_rec[s] = True
	for t in g[s]:
		if not visited_rec[t]:
			visited_rec[t] = True
			prev_rec[t] = s
			DFS_rec(g, t)

#solving the maze using DFS stack
def DFS_stack(g, v):
	visited, prev = [False for b in range(len(g))], [-1 for a in range(len(g))] #visited var and previous state
	s = []
	s.append(v) #stack
	visited[v] = True
	while s!=[]: #as long as stack has something
		u = s.pop() #pop the newest value
		for t in g[u]:
			if not visited[t]: #non checked
				visited[t] = True
				prev[t] = u
				s.append(t) #push
	printPath(prev, len(g)-1) #print the path

#breadth first search
def BFS(g, v):
	visited, prev = [False for b in range(len(g))], [-1 for a in range(len(g))] #visited var and previous state
	q = queue.Queue(10) #declare Queue
	q.put(v) #enqueue
	visited[v] = True
	while not q.empty(): #has something
		u = q.get() #dequeue
		for t in g[u]:
			if not visited[t]: #non checked
				visited[t] = True
				prev[t] = u
				q.put(t) #enqueu
	printPath(prev, len(g)-1) #print the path

#check if maze is unique or not
def checkValidRemove(r, c):
	if r==c-1:
		print("There is a unique path from source to destination.")
	elif r<c-1:
		print("A path from source to destination is not guarateed to exist.")
	else:
		print("There is at least one path from source to destination.")

#Find with path compression
def find_c(S,i):
    if S[i]<0:
        return i
    r = find_c(S,S[i])
    S[i] = r
    return r

# Returns root of tree that i belongs to
def find(S,i):
    if S[i]<0:
        return i
    return find(S,S[i])

# Joins i's tree and j's tree with compressed manner, if they are different
def union_c(S,i,j):
	ri = find_c(S,i)
	rj = find_c(S,j)
	if ri!=rj: # Do nothing if i and j belong to the same set
		S[rj] = ri
		return True #return true since i and j joined
	return False

# Joins i's tree and j's tree, if they are different
def union(S,i,j):
	ri = find(S,i)
	rj = find(S,j)
	if ri!=rj: # Do nothing if i and j belong to the same set
		S[rj] = ri  # Make j's root point to i's root
		return True #return true since i and j joined
	return False

#create a array(dsf) with give size
def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1

#return the number of sets in S
def count_sets(S):
	c = 0
	for i in S:
		if i==-1:
			c+=1
	return c

#draw maze
def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off')
    ax.set_aspect(1.0)

#create a list with
def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

#create full Adjacency List
def createFullAL(row, col):
	g = [[] for a in range(row*col)] #row x col
	for r in range(row):
		for c in range(col):
			cell = c + r*col
			if r!=0: #down
				g[cell].append(cell-col)
			if cell%col!=0: #left
				g[cell].append(cell-1)
			if c!=(col-1): #right
				g[cell].append(cell+1)
			if r!=row-1:
				g[cell].append(cell+col)
	return g

#create Adjacencylist
def createAL(r, c, w):
	g = createFullAL(r, c)
	for i in w:
		g[i[0]].remove(i[1]) #remove
		g[i[1]].remove(i[0]) #remove
	return g

plt.close("all")
maze_rows = 13
maze_cols = 8

print("There are ", (maze_rows*maze_cols), "cells.")
rev = int(input("How many walls whould you like to remove?\t"))
op = int(input("Type 1 to use standard union, type 2 to use union with path compressions.\t"))

walls = wall_list(maze_rows,maze_cols) #create a maze separeated by walls

S = DisjointSetForest(maze_rows*maze_cols) #create dsf to create maze

#part 1
checkValidRemove(rev, (maze_cols*maze_rows))
while count_sets(S)>1 : #while there are more than 1 set
	d = random.randint(0, len(walls)-1) #get random index
	if op==1: #standard union
		if union(S, walls[d][0], walls[d][1]): #if two numbers were in different sets
			walls.pop(d) #remove
	elif op==2: #union with path compression
		if union_c(S, walls[d][0], walls[d][1]): #if two numbers were in different sets
			walls.pop(d) #remove
	else: #exit program
		sys.exit("You chose the wrong input number!")

#part2
g = createAL(maze_rows, maze_cols, walls) #create Adjacency list with given maze
print("Adjacency List: ", g)

s0 = time.time()*1000
#part3-a
print("\nUsing BFS: 0", end='')
BFS(g, 0) #breadth first search
s1 = time.time()*1000
print("\nRuntime of BFS: ", round((s1-s0), 4), "s.")

#part3-b
print("\nUsing DFS stack: 0", end='')
DFS_stack(g, 0) #depth first search - stack
s2 = time.time()*1000
print("\nRuntime of DFS - stack ver.: ", round((s2-s1), 4), "s.")

#part3-c
visited_rec, prev_rec = [False for b in range(len(g))], [-1 for a in range(len(g))]
DFS_rec(g, 0) #depth first search - recursion
print("\nUsing DFS recursiong: 0", end='')
printPath(prev_rec, (maze_cols*maze_rows)-1) #printing the path
s3 = time.time()*1000
print("\nRuntime of DFS - recursion ver.: ", round((s3-s2), 4), "s.")

draw_maze(walls, maze_rows, maze_cols, cell_nums=True) #completed draw maze
plt.show()
