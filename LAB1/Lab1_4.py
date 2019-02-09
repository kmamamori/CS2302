"""
Lab1 - PART 4
2/9/2019 - Ken Amamori
CS2302 MW 10:30 - 11:50
"""
#importing libraries
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

#ax, center: centre, rad: radius of a circle
def circle(ax,center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    ax.plot(x,y,color='k') #draw the circle
    
plt.close("all") #clse a figure window
fig, ax = plt.subplots()

#a method named draw_circles(ax, number of 5circles set, center, rad)
draw_5circles(ax, 2, [0,0], 100) #for 4a
#draw_5circles(ax, 3, [0,0], 100) #for 4b
#draw_5circles(ax, 4, [0,0], 100) #for 4c

ax.set_aspect(1.0) #x:y=1:1
ax.axis('off') #include x,y-axis
plt.show() #display figure
#fig.savefig('lab1_4a.png')
