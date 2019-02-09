"""
Lab1 - PART 1
2/9/2019 - Ken Amamori
CS2302 MW 10:30 - 11:50
"""
#importing libraries
import matplotlib.pyplot as plt
import numpy as np
import math

#c: center of the square, r: radius, n: base case, n layers
def draw_squares(ax,c,r,n):
    if n>0: #base case: as long as n greater than 0
        p=np.array([[c[0]-r,c[1]-r], [c[0]+r,c[1]-r], [c[0]+r,c[1]+r], [c[0]-r,c[1]+r], [c[0]-r,c[1]-r]]) #get the four points of square based on 'Center' and 'r'
        ax.plot(p[:,0],p[:,1],color='k') #draw a square with given array P
        draw_squares(ax, [c[0]-r, c[1]-r], r/2, n-1) #left bottom with halfed rad
        draw_squares(ax, [c[0]+r, c[1]-r], r/2, n-1) #right bottom with halfed rad
        draw_squares(ax, [c[0]+r, c[1]+r], r/2, n-1) #right above with halfed rad
        draw_squares(ax, [c[0]-r, c[1]+r], r/2, n-1) #left above with halfed rad

plt.close("all") #clse a figure window
fig, ax = plt.subplots()

#calling a method "draw_squares" with ax, center coordinate, radius, number of recusive method
draw_squares(ax,[500,500],500,2) #for 1a 
#draw_squares(ax,[500,500],500,3) #for 1b
#draw_squares(ax,[500,500],500,4) #for 1c

ax.set_aspect(1.0) #x:y=1:1
ax.axis('off') #x,y-axis
plt.show() #display figure
#fig.savefig('lab1_1a.png') #save the figure
