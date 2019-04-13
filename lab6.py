"""""""""""""""""""""""""""""""""""""""
Lab 6 - Disjoint Set Forest - Create a maze
04/1/2019 - Ken M. Amamori
CS2302 MW 10:30 - 11:50
Professor: Olac Fuentes
TA: Anindita Nath, Maliheh Zargaran
"""""""""""""""""""""""""""""""""""""""
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import interpolate
import time

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

plt.close("all")
maze_rows = 10
maze_cols = 15

walls = wall_list(maze_rows,maze_cols) #create a maze separeated by walls
draw_maze(walls,maze_rows,maze_cols,cell_nums=True)  #draw maze with number in each cell

start = time.time()*1000 #get the starting time
S = DisjointSetForest(maze_rows*maze_cols) #create dsf to create maze
while count_sets(S)>1: #while there are more than 1 set
	d = random.randint(0, len(walls)-1) #get random index
	if union(S, walls[d][0], walls[d][1]): #if two numbers were in different sets
		walls.pop(d) #remove

end = time.time()*1000 #get the ending time
print("Time: ", round(end-start, 4), "milisecons.") #
draw_maze(walls, maze_rows, maze_cols) #completed draw maze
plt.show()
