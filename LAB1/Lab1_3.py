"""
Lab1 - PART 3
2/9/2019 - Ken Amamori
CS2302 MW 10:30 - 11:50
"""
#importing libraries
import matplotlib.pyplot as plt
import numpy as np
import math

#ax: , c: root, n: depths, dx,dy: difference from root to the child in x-, y-axis 
def draw_tree(ax, c, n, dx, dy):
    if n>0:
        ax.plot([c[0],c[0]-dx],[c[1],c[1]-dy], color='k') #draw a line from the root  to the left child
        ax.plot([c[0],c[0]+dx],[c[1],c[1]-dy], color='k') #draw a line from the root  to the right child
        draw_tree(ax,[c[0]-dx,c[1]-dy],n-1,dx*0.5,dy*0.9) #call a recursive call with new root(left child) and change the deltaX & Y
        draw_tree(ax,[c[0]+dx,c[1]-dy],n-1,dx*0.5,dy*0.9) #call a recursive call with new root(right child) and change the deltaX & Y

plt.close("all") #clse a figure window
fig, ax = plt.subplots()

c=np.array([0,0]) #starting root coordinate
draw_tree(ax, c, 3, 50, 50) #for 3a
#draw_tree(ax, c, 4, 50, 50) #for 3b
#draw_tree(ax, c, 7, 50, 50) #for 3c

ax.set_aspect(1.0) #x:y=1:1
ax.axis('off') #include x,y-axis
plt.show() #display figure
#fig.savefig('lab1_3a.png')
