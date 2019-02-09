"""
Lab1 - All included.
2/9/2019 - Ken Amamori
CS2302 MW 10:30 - 11:50
"""
import matplotlib.pyplot as plt
import numpy as np
import math

def draw_5circles(ax, n, center, rad):
    if n>0:
        newrad = rad/3 #new radius
        circle(ax,[center[0]+rad-newrad,center[1]],newrad) #draw a circle: right
        draw_5circles(ax,n-1,[center[0]+rad-newrad,center[1]],newrad) #call a recusive method with new center and rad

        circle(ax,[center[0]-rad+newrad,center[1]],newrad) #draw a circle: left
        draw_5circles(ax,n-1,[center[0]-rad+newrad,center[1]],newrad)#call a recusive method with new center and rad

        circle(ax,center,newrad) #draw a circle: center
        draw_5circles(ax,n-1,center,newrad) #call a recusive method with same center and rad

        circle(ax,[center[0],center[1]+rad-newrad],newrad) #draw a circle: up
        draw_5circles(ax,n-1,[center[0],center[1]+rad-newrad],newrad) #call a recusive method with new center and rad

        circle(ax,[center[0],center[1]-rad+newrad],newrad) #draw a circle: down
        draw_5circles(ax,n-1,[center[0],center[1]-rad+newrad],newrad) #call a recusive method with new center and rad

    circle(ax,center,rad) #big circle

#ax: , c: root, n: depths, dx,dy: difference from root to the child in x-, y-axis 
def draw_tree(ax, c, n, dx, dy):
    if n>0:
        ax.plot([c[0],c[0]-dx],[c[1],c[1]-dy], color='k') #draw a line from the root  to the left child
        ax.plot([c[0],c[0]+dx],[c[1],c[1]-dy], color='k') #draw a line from the root  to the right child
        draw_tree(ax,[c[0]-dx,c[1]-dy],n-1,dx*0.5,dy*0.9) #call a recursive call with new root(left child) and change the deltaX & Y
        draw_tree(ax,[c[0]+dx,c[1]-dy],n-1,dx*0.5,dy*0.9) #call a recursive call with new root(right child) and change the deltaX & Y


#ax, center: centre, rad: radius of a circle
def circle(ax,center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    ax.plot(x,y,color='k') #draw the circle

#n times, centre, radius, next circle line
def draw_circles(ax,n,center,radius,w):
    if n>0:
        circle(ax,center,radius) #draw a circle with given center and radius
        draw_circles(ax,n-1,[center[0]*w,center[1]],radius*w,w) #call the method with new center and radius

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

#for part 1
#calling a method "draw_squares" with ax, center coordinate, radius, number of recusive method
draw_squares(ax,[500,500],500,2) #for 1a 
#draw_squares(ax,[500,500],500,3) #for 1b
#draw_squares(ax,[500,500],500,4) #for 1c

#for part 2
#call a method called draw_circles(ax, number of circles, centre, radius, interval)
#draw_circles(ax, 10, [100,0], 100,.6) #for 2a
#draw_circles(ax, 50, [100,0], 100,.9) #for 2b
#draw_circles(ax, 100, [100,0], 100,.95) #for 2c

#part 3
c=np.array([0,0]) #starting root coordinate
#draw_tree(ax, c, 3, 50, 50) #for 3a
#draw_tree(ax, c, 4, 50, 50) #for 3b
#draw_tree(ax, c, 7, 50, 50) #for 3c

#part 4
#a method named draw_circles(ax, number of 5circles set, center, rad)
#draw_5circles(ax, 2, [0,0], 100) #for 4a
#draw_5circles(ax, 3, [0,0], 100) #for 4b
#draw_5circles(ax, 4, [0,0], 100) #for 4c

ax.set_aspect(1.0) #x:y=1:1
ax.axis('on')
plt.show() #dispaly figure
#fig.savefig('lab1_2c.png')
